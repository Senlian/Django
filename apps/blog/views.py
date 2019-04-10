from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_deny

# Create your views here.
@xframe_options_deny
def BlogIndexView(request):
    return render(request, 'index.html', {'title': '首页', 'site_title': '博客网站'})
