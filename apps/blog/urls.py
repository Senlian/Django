#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import re_path
from . import views

app_name = 'blog'
urlpatterns = [
    # 首页展示
    re_path(r'^$', views.IndexView.as_view(), name='index'),
]
