#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views

config = {
    'width': '90%',
    'height': 500,
    'toolbar': ["undo", "redo", "|",
                "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                "h1", "h2", "h3", "h4", "h5", "h6", "|",
                "list-ul", "list-ol", "hr", "|",
                "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
                "emoji", "html-entities", "pagebreak", "|",
                "goto-line", "watch", "preview", "fullscreen", "clear", "search", "|",
                "help", "info"],
    'upload_image_formats': ["jpg", "JPG", "jpeg", "JPEG", "gif", "GIF", "png",
                             "PNG", "bmp", "BMP", "webp", "WEBP"],
    'image_floder': 'editor',
    'theme': 'default',  # dark / default
    'preview_theme': 'default',  # dark / default
    'editor_theme': 'default',  # pastel-on-dark / default
    'toolbar_autofixed': True,
    'search_replace': True,
    'emoji': True,
    'tex': True,
    'flow_chart': True,
    'sequence': True,
    'language': 'zh'  # zh / en
}

app_name = 'blog'
urlpatterns = [
    # 首页展示
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^markdown$', auth_views.TemplateView.as_view(template_name='markdown/markdown_view.html',extra_context={'config':config}), name='markdown'),
    re_path(r'^verify$', views.DrawVerifyView, name='verify'),
]
