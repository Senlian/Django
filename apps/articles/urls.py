#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import re_path, reverse_lazy, path
from django.contrib.auth import views as auth_views

from articles import views

app_name = 'articles'

urlpatterns = [
    re_path(r'^search/$', views.ArticleSearchView.as_view(), name='search'),
    re_path(r'^list/$', views.ArticleBackListView.as_view(), name='back'),
    re_path(r'^list/(?P<username>\w+)/$', views.ArticleListView.as_view(), name='list'),
    re_path(r'^show/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ArticleShowView.as_view(), name='show'),
    re_path(r'^actions/$', views.ArticleActionsView.as_view(), name='actions')
]
