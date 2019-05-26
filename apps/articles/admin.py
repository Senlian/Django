from django.contrib import admin
from articles.models import Articles, ArticleColumns, ArticleTags, ArticleComments


# Register your models here.

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'body', 'slug', 'created', 'update']
    list_display_links = ['author', 'title', 'body']
    list_filter = ('author', 'title', 'created', 'update')
    search_fields = ('author', 'title', 'body')
    # 连表查询是否自动select_related
    list_select_related = False
    # 每页显示条数
    list_per_page = 10
    # 页面总数小于等于list_max_show_all时在管理界面下方提示‘显示全部’
    list_max_show_all = 50
    date_hierarchy = 'update'
    save_on_top = True
    preserve_filters = False
    filter_horizontal = ('tags', 'likes', 'favorites',)

    fieldsets = (
        ('', {
            'fields': ('author', 'status', 'column'),
            # 'description': '账号注册信息'
        }),
        ('', {
            'fields': (('title', 'allowreply', 'top'), 'body'),
            # 'description': '账户权限信息'
        }),
        ('', {
            'fields': ('tags', ('likes', 'favorites'),),
            # 'description': '用户的基本资料'
        }))


@admin.register(ArticleColumns)
class ArticleColumnsAdmin(admin.ModelAdmin):
    list_display = ['author', 'body', 'created', 'update']
    list_display_links = ['author', 'body']
    list_filter = ('author', 'body', 'created', 'update')
    search_fields = ('author', 'body')
    # 连表查询是否自动select_related
    list_select_related = False
    # 每页显示条数
    list_per_page = 10
    # 页面总数小于等于list_max_show_all时在管理界面下方提示‘显示全部’
    list_max_show_all = 50
    date_hierarchy = 'update'
    save_on_top = True
    preserve_filters = False
    fields = ('author', 'body',)


@admin.register(ArticleTags)
class ArticleTagsAdmin(admin.ModelAdmin):
    list_display = ['author', 'body', 'created', 'update']
    list_display_links = ['author', 'body']
    list_filter = ('author', 'body', 'created', 'update')
    search_fields = ('author', 'body')
    # 连表查询是否自动select_related
    list_select_related = False
    # 每页显示条数
    list_per_page = 10
    # 页面总数小于等于list_max_show_all时在管理界面下方提示‘显示全部’
    list_max_show_all = 50
    date_hierarchy = 'update'
    save_on_top = True
    preserve_filters = False
    fields = ('author', 'body',)


@admin.register(ArticleComments)
class ArticleCommentsAdmin(admin.ModelAdmin):
    list_display = ['author', 'article', 'body', 'created']
    list_display_links = ['author', 'article', 'body']
    list_filter = ('author', 'article', 'body', 'created')
    search_fields = ('author', 'article', 'body')
    # 连表查询是否自动select_related
    list_select_related = False
    # 每页显示条数
    list_per_page = 10
    # 页面总数小于等于list_max_show_all时在管理界面下方提示‘显示全部’
    list_max_show_all = 50
    date_hierarchy = 'created'
    save_on_top = True
    preserve_filters = False
    fields = ('author', 'article', 'body',)
