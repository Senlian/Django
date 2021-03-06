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

    re_path(r'^user-center-info/$', views.UserCenterInfoView.as_view(), name='uc_info'),
    re_path(r'^user-center-collects/$', views.UserCenterCollectsView.as_view(), name='uc_collects'),
    re_path(r'^user-center-focus/$', views.UserCenterFocusView.as_view(), name='uc_focus'),
    re_path(r'^user-center-fans/$', views.UserCenterFansView.as_view(), name='uc_fans'),

    re_path(r'^user-center-photos/$', views.UserCenterPhotosView.as_view(), name='uc_photos'),
    re_path(r'^user-center-news/$', views.UserCenterNewsView.as_view(), name='uc_news'),

    re_path(r'^user-center-edit-protrait/$', views.UserCenterEditProtraitView.as_view(), name='uc_edit_protrait'),
    re_path(r'^user-center-edit-info/$', views.UserCenterEditInfoView.as_view(), name='uc_edit_info'),

    re_path(r'^accounts-manager-info/$', views.AccountsManagerInfoView.as_view(), name='am_info'),
]
