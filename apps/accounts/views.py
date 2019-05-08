from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render, resolve_url
from django.contrib.auth import login as auth_login
from django.contrib.auth import views as auth_views
from django.contrib.sites.shortcuts import get_current_site
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.utils.http import is_safe_url, urlsafe_base64_decode

from .forms import AccountsLoginForm, AccountRegisterForm
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
        site_name = current_site.name
        domain = current_site.domain
        protocol = 'https://' if self.request.is_secure() else 'http://'
        uri = protocol + domain
        if new_user.email:
            message = """<p><span>恭喜您注册成为<a href='{0}'>本站</a>会员,网站地址:<a href='{1}'>{1}</a>。</span><br>
            <span style="font-weight: bold;">账号：<span style="color: red;font-weight: bold;">{2}</span></span><br>
            <span style="font-weight: bold;">密码：<span style="color: red;font-weight: bold;">{3}</span></span><br>
            <span>为了您的账户安全，请勿将账号和密码告知他人！！</span></p>""".format(uri, uri, new_user.username, password)
            new_user.email_user(subject='注册成功通知', message='', html_message=message,
                                from_email=settings.DEFAULT_FROM_EMAIL, fail_silently=True)

        success_url = self.get_success_url()
        return JsonResponse({'success_url': success_url})
