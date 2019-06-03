#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'blog'
urlpatterns = [
    # 首页展示
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^markdown$', views.MarkDownView.as_view(), name='markdown'),
    re_path(r'^verify$', views.DrawVerifyView, name='verify'),
]
