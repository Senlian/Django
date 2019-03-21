#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# @license    : (C) Copyright 2013-{YEAR}, Node Supply Chain Manager Corporation Limited.
# @author     : Administrator
# @Email      :
# @Time       : 2019/3/13 14:36
# @File       : urls.py
# @Software   : PyCharm
# @Modules     :python3 -m pip install 
# @Desc       : 
'''
from django.urls import path, re_path, include
from django.urls import reverse_lazy
from . import views, list_views
from django.views.generic.base import RedirectView

app_name = 'article'

urlpatterns = [
    re_path(r'^article_column/$', views.article_column, name='article_column'),
    re_path(r'^rename_column/$', views.rename_article_column, name='rename_column'),
    re_path(r'^del_column/$', views.del_article_column, name='del_column'),
    re_path(r'^article_post/$', views.article_post, name='article_post'),
    re_path('^article_list/$', views.article_list, name='article_list'),
    re_path(r'^article_detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.article_detail, name='article_detail'),
    re_path(r'^article_del/$', views.article_del, name='article_del'),
    re_path(r'^article_edit/(?P<article_id>\d+)/$', views.article_edit, name='article_edit'),
    re_path(r'^article_titles/$', list_views.article_titles, name='article_titles'),
    re_path(r'^article_titles/(?P<username>[-\w]+)/$', list_views.article_titles, name='author_articles'),
    re_path(r'^article_like/$', list_views.article_like, name='article_like'),
    re_path(r'^article_tag/$', views.article_tag, name='article_tag'),
    re_path(r'^rename_tag/$', views.rename_tag, name='rename_tag'),
    re_path(r'^del_tag/(?P<tag_id>\d+)/$', views.del_tag, name='del_tag')
]

if __name__ == '__main__':
    pass
