#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import re_path, reverse_lazy, path
from django.contrib.auth import views as auth_views

from articles import views

app_name = 'articles'

urlpatterns = [
    re_path(r'^search/$', auth_views.TemplateView.as_view(), name='search'),
    re_path(r'^back_stage/$', views.ArticleListTitleView.as_view(), name='back'),
    re_path(r'^show/(?P<id>\d+)/(?P<slug>[-\w]+)/>$', views.ArticleShowView.as_view(), name='show')
]
