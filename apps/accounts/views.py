from django.conf import settings
from django.urls import reverse_lazy, resolve
from django.utils.encoding import force_bytes
from django.shortcuts import render, resolve_url, reverse, redirect
from django.contrib.auth import update_session_auth_hash, logout as auth_logout, login as auth_login
from django.contrib.auth import views as auth_views
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.utils.http import is_safe_url, urlsafe_base64_decode, urlsafe_base64_encode

import random, string

from .forms import (AccountsLoginForm, AccountsRegisterForm, AccountsEmailForm, AccountsSetPasswordForm,
                    AccountsChangePwdForm)
from blog.views import DrawVerifyView


# Create your views here.
class AccountsLoginFormMixin:
    def form_valid(self, form):
        # 表单验证通过，用户登录
        auth_login(self.request, form.get_user())
        success_url = self.get_success_url()
        return JsonResponse({'success_url': success_url})


class AccountsRegisterFormMixin:
    success_url_allowed_hosts = set()

    def get_success_url_allowed_hosts(self):
        return {self.request.get_host(), *self.success_url_allowed_hosts}

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url(settings.LOGIN_REDIRECT_URL)

    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        url_is_safe = is_safe_url(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ''


class LoginView(AccountsLoginFormMixin, auth_views.LoginView):
    # 模板
    template_name = 'accounts/login.html'
    # 模板表单
    form_class = AccountsLoginForm
    # 表单渲染数据=form+extra_context
    extra_context = {'title': '登录', 'site_header': '用户名密码登录', 'site_title': '账号管理'}
    redirect_field_name = reverse_lazy('blog:index')

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        if request.user.is_authenticated:
            return redirect('blog:index')
        DrawVerifyView(request)
        return self.render_to_response(self.get_context_data())


class RegisterView(AccountsRegisterFormMixin, auth_views.FormView):
    # 模板
    template_name = 'accounts/register.html'
    # 模板表单
    form_class = AccountsRegisterForm
    # 表单渲染数据=form+extra_context
    extra_context = {'title': '注册', 'site_header': '账号注册', 'site_title': '账号管理'}
    redirect_field_name = reverse_lazy('blog:index')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        password = form.cleaned_data['password']
        new_user.set_password(password)
        new_user.save()
        form.save_m2m()
        auth_login(self.request, new_user)
        current_site = get_current_site(self.request)
        # site_name = current_site.name
        domain = current_site.domain
        protocol = 'https://' if self.request.is_secure() else 'http://'
        uri = protocol + domain
        if new_user.email:
            html_message = """<p><span>恭喜您注册成为<a href='{0}'>本站</a>会员,网站地址:<a href='{1}'>{1}</a>。</span><br>
            <span style="font-weight: bold;">账号：<span style="color: red;font-weight: bold;">{2}</span></span><br>
            <span style="font-weight: bold;">密码：<span style="color: red;font-weight: bold;">{3}</span></span><br>
            <span>为了您的账户安全，请勿将账号和密码告知他人！！</span></p>""".format(uri, uri, new_user.username, password)
            try:
                new_user.email_user(subject='注册成功通知', message='', html_message=html_message,
                                    from_email=settings.DEFAULT_FROM_EMAIL, fail_silently=True)
            except Exception as e:
                print(e)
        success_url = self.get_success_url()
        return JsonResponse({'success_url': success_url})


class ResetPasswordView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/reset.html'
    form_class = AccountsSetPasswordForm
    success_url = reverse_lazy('blog:index')
    post_reset_login = True
    extra_context = {'title': '重设密码', 'site_header': '重设密码', 'site_title': '账号管理'}

    def form_valid(self, form):
        user = form.save()
        # 链接失效
        del self.request.session[auth_views.INTERNAL_RESET_SESSION_TOKEN]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        success_url = self.get_success_url()
        return JsonResponse({'success_url': success_url})


class ChangePasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/reset.html'
    form_class = AccountsChangePwdForm
    success_url = reverse_lazy('blog:index')
    post_reset_login = False
    extra_context = {'title': '修改密码', 'site_header': '修改密码', 'site_title': '账号管理'}

    def form_valid(self, form):
        # 密码修改
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        success_url = self.get_success_url()
        if not self.post_reset_login:
            auth_logout(self.request)
        return JsonResponse({'success_url': success_url})


class SendEmailView(auth_views.FormView):
    form_class = AccountsEmailForm
    success_url = reverse_lazy('blog:index')
    template_name = 'accounts/send_email.html'
    extra_context = {'title': '重设通知', 'site_header': '重设通知', 'site_title': '账号管理'}

    def form_valid(self, form):
        current_site = get_current_site(self.request)
        # site_name = current_site.name
        domain = current_site.domain
        protocol = 'https://' if self.request.is_secure() else 'http://'
        uri = protocol + domain

        is_staff = form.cleaned_data['is_staff']
        if is_staff:
            is_send = self.send_reset(uri, form)
        else:
            is_send = self.send_verify(uri, form)

        return JsonResponse({'is_send': is_send, 'timer': settings.EMAIL_TIMER})

    def form_invalid(self, form):
        is_staff = form.cleaned_data['is_staff']
        if not is_staff:
            return HttpResponse(form.errors.as_text().split('*')[-1])
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def send_reset(self, uri, form):
        subject = '密码重设通知'
        # 获取账户信息
        user = form.get_user()
        # base64位加密
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)
        reset_uri = uri + resolve_url('accounts:reset', uidb64=uid, token=token)
        html_message = """<p><span>您正在申请重设<a href='{0}'>本站</a>的登录密码,网站地址:<a href='{0}'>{0}</a>。</span><br>
        <span>请点击访问下方链接重新设置您的登录密码：<br><blockquote><a href='{1}'>{1}</a></blockquote></span><br>
        <span>如您已忘记本站账号，账号为 <span style="color: blue;font-weight: bold;">{2}</span> ,</span>
        <span>如非本人操作，请忽略。</span></p>""".format(uri, reset_uri, user.username)
        opts = {
            'subject': subject,
            'html_message': html_message,
        }
        return form.send_email(**opts)

    def send_verify(self, uri, form, TIMER=None):
        TIMER = TIMER or settings.EMAIL_TIMER
        email = form.cleaned_data['email'].strip().lower()
        subject = '邮箱验证通知'
        verify = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
        form.set_cache('register_verify_{0}'.format(email.split('@')[0]), verify, TIMER)
        html_message = """<p><span>您正在使用该邮箱注册<a href='{0}'>本站</a>的会员,网站地址:<a href='{0}'>{0}</a>。</span><br>
        <span>为保证是您本人进行的注册操作，特发送此邮件进行验证，</span>
        <span>请输入验证码 <span style="color: red;font-weight: bold;">{1}</span> 并在<span style="color: blue;font-weight: bold;">{2}秒</span>内完成您的注册。</span><br>
        <span>如非本人操作，请忽略。</span><br></p>""".format(uri, verify, TIMER)
        opts = {
            'subject': subject,
            'html_message': html_message,
        }
        return form.send_email(**opts)


class UserInfoView(auth_views.TemplateView):
    template_name = 'accounts/userinfo.html'
    extra_context = {'title': '我的资料', 'site_title': '个人中心-SCSDN', 'site_header': '个人资料'}
