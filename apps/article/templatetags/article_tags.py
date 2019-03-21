#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# @license    : (C) Copyright 2013-{YEAR}, Node Supply Chain Manager Corporation Limited.
# @author     : Administrator
# @Email      :
# @Time       : 2019/3/20 17:17
# @File       : article_tags.py
# @Software   : PyCharm
# @Modules     :python3 -m pip install 
# @Desc       : 
'''
from django import template
from django.db.models import Count
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()
from article.models import ArticlePost


@register.simple_tag
def article_count():
    return ArticlePost.objects.count()


@register.simple_tag
def author_article_count(user):
    return user.article.count()


@register.inclusion_tag(filename='article/last_articles.html')
def last_articles(n=1):
    last_articles = ArticlePost.objects.order_by('-created')[:n]
    return {'last_articles': last_articles}


@register.simple_tag(name='most_comment_articles')
def most_comment_articles(n=1):
    # ArticleComments数据模型以字段comments绑定外键ArticlePost，
    # 因此ArticlePost可以通过这个字段统计评论总数，
    # annotate给ArticlePost添加total_comments属性，标记评论总数
    return ArticlePost.objects.annotate(total_comments=Count('comments').order_by('-total_comments')[:n])

@register.filter(name='markdown')
def markdown_tag(text):
    import markdown
    return mark_safe(markdown.markdown(text))