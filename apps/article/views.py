from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def ArticleIndexView(request):
    return render(request, 'index.html', {'title': '首页', 'site_title': '博客网站'})
