#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import forms
from django.db.models import Q
from django.forms import widgets
from articles.models import Articles


# TODO：搜索表单
class ArticleSearchForm(forms.Form):
    search = forms.CharField(max_length=256, label="搜索内容", widget=widgets.TextInput(
        attrs={
            'type': 'search',
            'class': 'form-control mr-sm-2',
            'aria-label': 'Search',
            'requred': False,
            'placeholder': '搜SCSDN'
        }))

    def clean_search(self):
        search = self.cleaned_data['search']
        articles = Articles.objects.filter(
            Q(author__username__icontains=search) | Q(author__nick_name__icontains=search) | Q(
                title__icontains=search) | Q(body__contains=search) | Q(column__body__contains=search) | Q(
                tags__body__contains=search))
        if articles:
            return articles
        else:
            raise forms.ValidationError('搜索结果为空')
