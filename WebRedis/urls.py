from django.conf.urls import url
from . import views
app_name = 'WebRedis'

urlpatterns = [
    url(r'^$', views.indexpage, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.loginpage, name='login'),
    url(r'^logout/$', views.logoutpage, name='logout'),
    url(r'^verify/$', views.verify, name='verify'),
    url(r'^demo/$', views.demo, name='demo'),
]