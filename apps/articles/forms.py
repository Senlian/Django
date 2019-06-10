#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import forms
from django.db.models import Q
from django.forms import widgets
from articles.models import Articles, ArticleComments


# TODO：搜索表单
class ArticleSearchForm(forms.Form):
    search = forms.CharField(max_length=256, label="搜索内容", required=False, widget=widgets.TextInput(
        attrs={
            'type': 'search',
            'class': 'form-control mr-sm-2',
            'aria-label': 'Search',
            'placeholder': '搜SCSDN'
        }))

    def clean_search(self):
        search = self.cleaned_data['search'].strip()
        if search:
            articles = Articles.objects.filter(
                Q(author__username__icontains=search) |
                Q(author__nick_name__icontains=search) |
                Q(title__icontains=search) |
                Q(body__contains=search) |
                Q(column__body__contains=search) |
                Q(tags__body__contains=search))
        else:
            articles = Articles.objects.filter(status='1')
        if articles:
            return articles.order_by('-update')
        else:
            raise forms.ValidationError('搜索结果为空')


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'body')

        widgets = {
            'title': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '输入文章标题'
            })}


class ArticleCommentsForm(forms.ModelForm):
    # 此处注意 author指定的to_field字段为username
    class Meta:
        model = ArticleComments
        fields = ('author', 'article', 'body',)
