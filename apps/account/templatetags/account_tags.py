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
# from django.db.models import Count
# from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe, SafeText

register = template.Library()


@register.filter(name='add_class')
def add_class(text):
    if not isinstance(text, SafeText):
        return text
    return text.label_tag(attrs={'class':"col-sm-2 control-label  font-weight-bold"})