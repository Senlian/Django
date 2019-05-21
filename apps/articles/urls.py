#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import re_path, reverse_lazy, path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'articles'

urlpatterns = [
    re_path(r'^search$', auth_views.TemplateView.as_view(), name='search')
]
