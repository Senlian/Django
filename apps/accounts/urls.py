from django.urls import re_path, reverse_lazy,path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(next_page=reverse_lazy('blog:index')), name='logout'),
    re_path(r'^register/$', views.RegisterView.as_view(), name='register'),
    path('reset/<uidb64>/<token>/', views.ResetPasswordView.as_view(extra_context={
        'title': '修改密码', 'site_header': '修改密码', 'site_title': '账号管理'}), name='reset'),
    re_path(r'^send_email/$', views.SendEmailView.as_view(extra_context={
        'title': '重设密码', 'site_header': '重设密码', 'site_title': '账号管理'}), name='send_email'),
]
