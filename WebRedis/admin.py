from django.contrib import admin
from .models import UserInfoHandler, RedisHandler

# 修改登录网页标题
admin.site.site_title = "WebRedis超级后台"
# 修改登录窗口标题
admin.site.site_header = "WebRedis管理系统"


# Register your models here.
@admin.register(UserInfoHandler)
class UserInfoHandlerAdmin(admin.ModelAdmin):
    list_display = ["uid", "name", "phone", "email", "limits", "ctime", "mtime"]
    list_display_links = ["uid", "name", "phone", "email"]
    search_fields = ["uid", "name", "phone", "email"]
    list_filter = ["uid", "name", "phone", "email"]
    list_per_page = 20
    date_hierarchy = 'mtime'
    fieldsets = (
        ("帐号信息", {'fields': ["uid", "pwd"]}),
        ("个人信息", {'fields': ["name", "phone", "email"]}),
        ("权限信息", {'fields': ["limits"]}),
    )


@admin.register(RedisHandler)
class RedisHandlerAdmin(admin.ModelAdmin):
    # 显示选项
    list_display = ["host", "port", "name", "user", "color_set", "count", "uid", "describtion", "ctime", "mtime"]
    # 点击显示选项跳转编辑页面
    list_display_links = ["host", "port", "name", "user", "describtion"]
    # 不用跳转编辑页面，外层可编辑，不可与list_display_links有相同项
    # list_editable = ["status", "describtion"]
    # 搜索字段，搜索框中对那部分内容进行查找
    search_fields = ["host", "port", "user", "name", "uid"]
    # 右侧过滤器
    list_filter = ["host", "port", "user", "name", "uid"]
    # 一页多少条
    list_per_page = 20
    # 时间分层筛选
    date_hierarchy = 'mtime'
    # 添加编辑界面显示字段
    # fields = (("host", "port"),)
    # 添加编辑界面排除字段
    # exclude = ("host",)
    # 编辑界面分块
    fieldsets = (
        ("服务器信息", {'fields': ["host", "port", "name"]}),
        ("帐号信息", {'fields': ["user", "pwd"]}),
        ("状态", {'fields': ["count", "status"]}),
        ("其他", {'fields': ["uid", "describtion"]}),
    )

    # 设置编辑界面只读字段
    # readonly_fields = ["host", "port"]
    # def save_model(self, request, obj, form, change):
    #   pass
