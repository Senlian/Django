from django.contrib import admin
from .models import AccountUserProfileModel, AccountUserDetailModel

# 后台定义
admin.sites.AdminSite.title = '后台登录'
admin.sites.AdminSite.site_title = '管理员系统'
admin.sites.AdminSite.site_header = '后台登录'
admin.sites.AdminSite.index_title = '超管系统'


# Register your models here.
@admin.register(AccountUserProfileModel)
class AccountUserProfileModelAdmin(admin.ModelAdmin):
    # 数据管理界面显示列
    list_display = ['id', 'username', 'age', 'birth', 'sex', 'photo', 'created']
    list_display_links = ['sex']
    # 编辑列表页显示编辑框，字段不可属于list_display_links列表
    list_editable = ['birth', 'age']
    # 后台添加编辑页面的显示和排版方式，括号内单独成行
    # fields = (('age', 'birth'), 'sex', 'photo')
    # 定义管理界面右侧过滤器的过滤字段，必须为模型所属字段
    list_filter = ('sex', 'age')
    # 字段集，后台添加编辑页面分组排版，不可与fields共存
    # description显示在字段集标题下方
    list_max_show_all = 100
    list_per_page = 1
    # 一对一，多对一，多对多字段中的related_name字段
    list_select_related = ('user_detail',)
    
    fieldsets = (
        ('字段集标题1', {
            'fields': ('age', 'birth', 'sex',),
            'description': '字段集描述1'
        }),
        ('字段集标题2', {
            'fields': ('photo',),
            'description': '字段集描述2'
        }),
    )

    # date_hierarchy = 'created'

    # 空值替换符
    # empty_value_display = '-'

    def birth(self, obj):
        return obj.day

    birth.empty_value_display = 'ddd'


@admin.register(AccountUserDetailModel)
class AccountUserDetailModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'phone', 'profession', 'company', 'school', 'intro']
    list_display_links = ['phone', 'profession', 'company', 'school', 'intro']
    empty_value_display = '-'
