# -*- coding:utf-8 -*-
from django.contrib import admin
from WebRedis.models import dbServer


# Register your models here.
# 通过装饰器注册数据模型
@admin.register(dbServer)
class dbServerAdmin(admin.ModelAdmin):
    # 显示选项
    list_display = ["pid", "host", "port", "username", "colored_status", "describtion", "ctime"]
    # 点击显示选项跳转编辑页面
    list_display_links = ["pid", "host", "port", "username"]
    # 不用跳转编辑页面，外层可编辑，不可与list_display_links有相同项
    # list_editable = ["status", "describtion"]
    # 搜索字段，搜索框中对那部分内容进行查找
    search_fields = ["host", "port", "username"]
    # 右侧过滤器
    list_filter = ["host", "port", "username"]
    # 一页多少条
    list_per_page = 50
    # 时间分层筛选
    date_hierarchy = 'ctime'
    # 添加编辑界面显示字段
    # fields = (("host", "port"),)
    # 添加编辑界面排除字段
    # exclude = ("host",)
    # 编辑界面分块
    # fieldsets = (
    #     ("field1", {'fields':["host", "port"]}),
    #     ("field2", {'fields':["username", "passwd"]}),
    # )
    # 设置编辑界面只读字段
    # readonly_fields = ["host", "port"]
    # def save_model(self, request, obj, form, change):
    #     # 提交保存时的操作
    #     pass
    # def delete_model(self, request, obj):
    #     pass


# 注册装饰器的另一种方法
# admin.site.register(dbServer, dbServerAdmin)
# 修改登录网页标题
admin.site.site_title= "WebRedis超级后台"
# 修改登录窗口标题
admin.site.site_header= "WebRedis管理系统"

