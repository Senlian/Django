# -*- coding:utf-8 -*-
from django.apps import AppConfig
import os

default_app_config = "WebRedis.WebRedisConfig"


class WebRedisConfig(AppConfig):
    # WebRedis
    name = os.path.split(os.path.dirname(__file__))[1]
    verbose_name = "站点数据库管理"
