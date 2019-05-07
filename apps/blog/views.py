from django.shortcuts import render
from django.contrib.auth import views as auth_views


# Create your views here.

class IndexView(auth_views.TemplateView):
    template_name = 'blog/index.html'
    extra_context = {'title': 'SCSDN', 'site_title': '专业IT技术社区'}
