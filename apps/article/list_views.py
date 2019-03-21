#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# @license    : (C) Copyright 2013-{YEAR}, Node Supply Chain Manager Corporation Limited.
# @author     : Administrator
# @Email      :
# @Time       : 2019/3/19 11:44
# @File       : list_views.py
# @Software   : PyCharm
# @Modules     :python3 -m pip install 
# @Desc       : 
'''
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator

from .models import ArticleColumn, ArticlePost
from django.contrib.auth.models import User



def article_titles(request, username=None):
    if username:
        user = User.objects.get(username=username)
        articles = ArticlePost.objects.filter(author=user)
        try:
            userinfo = user.userinfo
        except:
            userinfo = None
    else:
        articles = ArticlePost.objects.all()
    pages = Paginator(articles, 2)
    page = request.GET.get('page')
    try:
        curpage = pages.page(page)
    except PageNotAnInteger:
        curpage = pages.page(1)
    except EmptyPage:
        curpage = pages.page(pages.num_pages)
    articles = curpage.object_list
    if username:
        return render(request, 'article/author_articles.html',
                      {'page': curpage, 'articles': articles, 'userinfo': userinfo, 'user': user})
    return render(request, 'article/article_titles.html', {'page': curpage, 'articles': articles})


@login_required(login_url=reverse_lazy('account:user_login'))
@require_POST
@method_decorator(csrf_exempt, name='POST')
def article_like(request):
    article_id = request.POST.get('id')
    action = request.POST.get('action')
    if article_id and action:
        try:
            article = ArticlePost.objects.get(id=article_id)
            if action == 'like':
                article.user_like.add(request.user)
                return HttpResponse('1')
            else:
                article.user_like.remove(request.user)
                return HttpResponse('2')
        except Exception as e:
            return HttpResponse('3')
    return HttpResponse('4')


if __name__ == '__main__':
    pass
