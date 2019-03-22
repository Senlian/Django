#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# @license    : (C) Copyright 2013-{YEAR}, Node Supply Chain Manager Corporation Limited.
# @author     : Administrator
# @Email      :
# @Time       : 2019/3/22 9:40
# @File       : forms.py
# @Software   : PyCharm
# @Modules     :python3 -m pip install 
# @Desc       : 
'''

from django import forms
from .models import Image
from slugify import slugify
from urllib import request
from django.core.files.base import ContentFile
import os


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['.jpg', '.jpeg', '.png']
        if os.path.splitext(url)[-1].lower() not in valid_extensions:
            raise forms.ValidationError('图片格式不支持！')
        return url

    def save(self, commit=True):
        image = super(ImageForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{0}.{1}'.format(slugify(image.title), image_url.rsplit('.', 1)[1].lower())
        response = request.urlopen(image_url)
        image.image.save(name=image_name, content=ContentFile(response.read()), save=False)
        if commit:
            image.save()
        return image