from django.urls import re_path, reverse_lazy, path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(next_page=reverse_lazy('blog:index')), name='logout'),
    re_path(r'^register/$', views.RegisterView.as_view(), name='register'),
    path('reset/<uidb64>/<token>/', views.ResetPasswordView.as_view(), name='reset'),
    re_path(r'^change/$', views.ChangePasswordView.as_view(), name='change'),
    re_path(r'^send_email/$', views.SendEmailView.as_view(), name='send_email'),

    re_path(r'^userinfo/$', views.UserInfoView.as_view(), name='userinfo'),
]
