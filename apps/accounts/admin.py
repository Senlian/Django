from django.contrib import admin
from .models import UserProfile


# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # 定义显示项
    list_display = ['username', 'is_superuser', 'email', 'phone', 'gender',
                    'name', 'age', 'profession', 'company', 'school', 'intro']
    # 定义可以跳转修改界面的显示项
    list_display_links = ['username', 'email', 'phone', 'profession', 'company', 'school', 'intro']
    # 右侧过滤栏字段
    list_filter = ('is_superuser','gender', 'profession', 'company', 'school')
    # 连表查询是否自动select_related
    list_select_related = False
    # 每页显示条数
    list_per_page = 10
    # 页面总数小于等于list_max_show_all时在管理界面下方提示‘显示全部’
    list_max_show_all = 50
    # 显示项表现为可编辑框，不可与list_display_links重复
    list_editable = ['gender']
    # 搜索框的搜索字段
    search_fields = ['username', 'email', 'phone', 'profession', 'company', 'school']
    # 对Date和DateTime类型进行搜索
    date_hierarchy = 'date_joined'
    # True,保存为新的
    # False,保存并增加另一个,默认
    save_as = False
    # 如果save_as为True,save_as_continue为True,点击`保存为新的`后继续编辑页面,默认
    # 如果save_as为True,save_as_continue为False,否则跳转到列表页面
    save_as_continue = True
    # True，编辑界面上方也显示保存按钮，默认False
    save_on_top = True
    # 定义分页插件
    # from django.core.paginator import Paginator
    # paginator=Paginator
    # 是否保留过滤器
    preserve_filters = False
    # 编辑页面对外键进行编辑
    # inlines = []

    '''编辑详情页模板
        add_form_template = None
        change_form_template = None
        change_list_template = None
        delete_confirmation_template = None
        delete_selected_confirmation_template = None
        object_history_template = None
        popup_response_template = None
    '''

    '''# 定义执行动作   
        def action():
            pass
        action.short_description = "动作名称"
        actions = [action,]
        # 动作框表单
        action_form = helpers.ActionForm
        # 上方显示
        actions_on_top = True
        # 下方显示
        actions_on_bottom = False
        # 显示选择个数
        actions_selection_counter = True
        # 检查设置项
        checks_class = ModelAdminChecks
    '''
    '''
        # 显示的FK和M2M,默认全部显示
        autocomplete_fields = ()
        # FK和M2M显示为<input>框，而非<select>
        raw_id_fields = ()
        # 编辑详情页面显示的字段
        fields = None
        # 编辑详情页排除显示的字段
        exclude = None
        # 编辑详情页分类显示,与fields不能共存
        fieldsets = None
        # 定制编辑详情页的表单
        form = forms.ModelForm
        # M2M字段竖向显示选择框和删除框
        filter_vertical = ()
        # M2M字段横向显示选择框和删除框
        filter_horizontal = ()
        # FK字段使用radio形式显示
        radio_fields = {}
        # 预填充字段
        prepopulated_fields = {}
        # 指定字段类型的显示组件，widget
        # 对于FK或M2M等关系字段要确认没有设置raw_id_fields，radio_fields或 autocomplete_fields
        formfield_overrides = {}
        # 只读字段，不可修改
        readonly_fields = ()
        # 排序字段
        ordering = None
        # 指定列表页点击哪些字段可以进行排序，默认list_display中的字段都可以
        sortable_by = None
        # True,调用模型的get_absolute_url方法，显示"View site"链接,也可以是get_absolute_url方法
        view_on_site = True
        # 过滤结果是否显示总数
        show_full_result_count = True
        # 检查设置项
        checks_class = BaseModelAdminChecks
    '''
    # fields = ['username', 'password', 'first_name', 'last_name', 'nick_name', 'is_superuser', 'groups',
    #           'user_permissions', 'is_staff', 'is_active', 'email', 'phone', 'gender',
    #           'profession', 'company', 'school', 'intro']

    fieldsets = (
        ('账户信息', {
            'fields': ('username', 'password', 'email', 'phone'),
            # 'description': '账号注册信息'
        }),
        ('账户权限', {
            'fields': ('is_superuser', 'is_staff', 'is_active', ('groups', 'user_permissions',)),
            # 'description': '账户权限信息'
        }),
        ('基本资料', {
            'fields': ('nick_name', 'first_name', 'last_name', 'birth', 'gender'),
            # 'description': '用户的基本资料'
        }),
        ('详细资料', {
            'fields': ('profession', 'company', 'school', 'intro'),
            # 'description': '用户的详细资料'
        }),
    )
    filter_horizontal = ('groups', 'user_permissions',)
