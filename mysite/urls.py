"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from .settings import DEBUG
from django.conf import settings
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.views import serve
from article import list_views
urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^home/', TemplateView.as_view(template_name='article/article_titles.html'), name='home'),
    re_path(r'^home/', list_views.article_titles, name='home'),
    re_path(r'^blog/', include('blog.urls', namespace='blog')),
    re_path(r'^account/', include('account.urls', namespace='account')),
    re_path(r'^article/', include('article.urls', namespace='article')),
    re_path(r'^mdeditor/', include('mdeditor.urls')),
    # 设置浏览器图标
    # re_path(r'^favicon\.ico$', RedirectView.as_view(url=r'static/images/logo.png'))
    # re_path(r'^favicon\.ico/$', serve, {'path':'images/logo.png'})
    path('favicon.ico', serve, {'path':'images/logo.png'})
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
