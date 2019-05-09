from django.urls import re_path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(next_page=reverse_lazy('blog:index')), name='logout'),
    re_path(r'^register/$', views.RegisterView.as_view(), name='register'),
    re_path(r'^reset/$', views.ResetPasswordView.as_view(), name='rest'),
    re_path(r'^emailto/$', views.EmailToView.as_view(extra_context={
        'title': '重设密码', 'site_header': '重设密码', 'site_title': '账号管理'}), name='emailto'),
]
