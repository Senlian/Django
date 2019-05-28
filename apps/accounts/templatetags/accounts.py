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


@register.filter(name=('is_uc_blogs'))
def isucmyblogs(url=None):
    if not url:
        return False
    if url.lower() == resolve_url('accounts:uc_blogs').lower():
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

