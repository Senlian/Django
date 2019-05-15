#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import template
from django.shortcuts import resolve_url

register = template.Library()


class SetVarNode(template.Node):
    def __init__(self, var, value, sign):
        self.var = var
        self.value = value
        self.sign = sign

    def render(self, context):
        try:
            if self.sign == '=':
                value = template.Variable(self.value).resolve(context)
            else:
                value = template.Variable(self.var).resolve(context)
            if self.sign == '+':
                context[self.var] = str(value)
            elif self.sign == '-':
                context[self.var] = str(-int(value))
            elif self.sign == '++':
                context[self.var] = str(int(value) + 1)
            elif self.sign == '--':
                context[self.var] = str(int(value) - 1)
            else:
                context[self.var] = str(self.value)
        except template.VariableDoesNotExist as e:
            return ""
        finally:
            return ""


@register.tag(name='set')
def set_var(parser, token):
    '''
    :param parser:
    :param token:
    :return:
    '''
    try:
        token_split = token.split_contents()
        print('token_split=', token_split)
        tag = token_split[0]
        value = 1
        if len(token_split) == 2:
            content = token_split[1]
            if '=' in content:
                sign = '='
                var, value = content.split('=')
            elif content[:1] in ['+', '-']:
                sign = content[:1]
                var = content[1:]
            elif content[-2:] in ['++', '--']:
                sign = content[-2:]
                var = content[:-2]
            else:
                return ''
        elif len(token_split) == 4:
            var, sign, value = token_split[1:]
        else:
            return ''
        return SetVarNode(var=var, value=value, sign=sign)

    except ValueError as e:
        msg = '%r tag requires a single argument' % tag
        raise template.TemplateSyntaxError(msg)


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
    if url.lower() == resolve_url('accounts:uc_info').lower():
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
