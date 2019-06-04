#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import template
from django.conf import settings
from django.shortcuts import resolve_url

register = template.Library()

@register.filter(name=('is_change'))
def ischange(url=None):
    if not url:
        return False
    if url.lower() == resolve_url('accounts:change').lower():
        return True
    return False


@register.filter(name=('is_uc_info'))
def isucinfo(url=None):
    if not url:
        return False
    if (url.lower() == resolve_url('accounts:uc_info').lower()) or \
            (url.lower() == resolve_url('accounts:uc_edit_info').lower()):
        return True
    return False


@register.filter(name=('is_uc_collects'))
def isuccollects(url=None):
    if not url:
        return False
    if url.lower() == resolve_url('accounts:uc_collects').lower():
        return True
    return False


@register.filter(name=('is_uc_focus'))
def isucfocus(url=None):
    if not url:
        return False
    if url.lower() == resolve_url('accounts:uc_focus').lower():
        return True
    return False


@register.filter(name=('is_uc_fans'))
def isucfans(url=None):
    if not url:
        return False
    if url.lower() == resolve_url('accounts:uc_fans').lower():
        return True
    return False


@register.filter(name=('is_uc_photos'))
def isucmyphotos(url=None):
    if not url:
        return False
    if url.lower() == resolve_url('accounts:uc_photos').lower():
        return True
    return False

@register.filter(name=('is_uc_news'))
def isucnews(url=None):
    if not url:
        return False
    if url.lower() == resolve_url('accounts:uc_news').lower():
        return True
    return False

@register.filter(name=('is_ac_back'))
def isacback(url=None):
    if not url:
        return False
    if url.lower() == resolve_url('articles:back').lower():
        return True
    return False

@register.filter(name=('is_ac_columns'))
def isaccolumns(url=None):
    if not url:
        return False
    if url.lower() == resolve_url('articles:columns').lower():
        return True
    return False

@register.filter(name=('is_ac_tags'))
def isactags(url=None):
    if not url:
        return False
    if url.lower() == resolve_url('articles:tags').lower():
        return True
    return False

@register.filter(name=('is_ac_comments'))
def isaccomments(url=None):
    if not url:
        return False
    if url.lower() == resolve_url('articles:comments').lower():
        return True
    return False


@register.filter(name=('is_am_info'))
def isaminfo(url=None):
    if not url:
        return False
    if url.lower() == resolve_url('accounts:am_info').lower():
        return True
    return False