from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render, resolve_url
from django.contrib.auth import login as auth_login
from django.contrib.auth import views as auth_views
from django.views.generic.edit import BaseFormView
from django.contrib.sites.shortcuts import get_current_site
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.utils.http import is_safe_url, urlsafe_base64_decode

import random, string

from .forms import AccountsLoginForm, AccountRegisterForm, AccountEmailForm
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
    extra_context = {'title': '登录', 'site_header': '用户名密码登录'}
    redirect_field_name = reverse_lazy('blog:index')

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        DrawVerifyView(request)
        return self.render_to_response(self.get_context_data())


class RegisterView(AccountsRegisterFormMixin, auth_views.FormView):
    # 模板
    template_name = 'accounts/register.html'
    # 模板表单
    form_class = AccountRegisterForm
    # 表单渲染数据=form+extra_context
    extra_context = {'title': '注册', 'site_header': '账号注册'}
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


class EmailToView(auth_views.FormView):
    form_class = AccountEmailForm
    success_url = reverse_lazy('blog:index')
    template_name = 'accounts/forget.html'

    def form_valid(self, form):
        current_site = get_current_site(self.request)
        # site_name = current_site.name
        domain = current_site.domain
        protocol = 'https://' if self.request.is_secure() else 'http://'
        uri = protocol + domain

        email = form.cleaned_data['email'].strip().lower()
        is_staff = form.cleaned_data['is_staff']
        TIMER = settings.EMAIL_TIMER
        try:
            if is_staff:
                subject = '密码重设通知'
                html_message = """<p><span>您正在申请重设<a href='{0}'>本站</a>的登录密码,网站地址:<a href='{0}'>{0}</a>。</span><br>
                <span>请点击访问下方链接重新设置您的登录密码：<br><blockquote><a href='{0}'>{0}</a></blockquote></span><br>
                <span>如您已忘记本站账号，账号为 <span style="color: blue;font-weight: bold;">{1}</span> ,</span>
                <span>如非本人操作，请忽略。</span></p>""".format(uri, form.get_user(email))
            else:
                subject = '邮箱验证通知'
                verify = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
                form.set_cache('register_verify_{0}'.format(email.split('@')[0]), verify, TIMER)
                html_message = """<p><span>您正在使用该邮箱注册<a href='{0}'>本站</a>的会员,网站地址:<a href='{0}'>{0}</a>。</span><br>
                <span>为保证是您本人进行的注册操作，特发送此邮件进行验证，</span>
                <span>请输入验证码 <span style="color: red;font-weight: bold;">{1}</span> 并在<span style="color: blue;font-weight: bold;">{2}秒</span>内完成您的注册。</span><br>
                <span>如非本人操作，请忽略。</span><br></p>""".format(uri, verify, TIMER)

            opts = {
                'subject': subject,
                'to_email': email,
                'html_message': html_message,
            }
            form.send_email(**opts)
        except Exception as e:
            print(e)
            raise e
        if not is_staff:
            return JsonResponse({'is_send': 'ok', 'timer': TIMER})
        else:
            return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print('dddddd')
        print(form.errors.as_text())
        return HttpResponse(form.errors.as_text().split('*')[-1])
