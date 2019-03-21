from django.contrib import admin
from .models import ArticleColumn, ArticlePost, ArticleComments, ArticleTag


# Register your models here.

@admin.register(ArticleColumn)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['user', 'column', 'created']
    list_filter = ['column']


@admin.register(ArticlePost)
class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'column', 'body', 'created']
    list_filter = ['column', 'author', 'created', 'title']
    list_display_links = ['author', 'title', 'column', 'body', 'created']


@admin.register(ArticleComments)
class ArticleCommentsAdmin(admin.ModelAdmin):
    list_display = ['article_id', 'author_id', 'body', 'created']
    list_display_links = ['body']


@admin.register(ArticleTag)
class ArticleCommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'author_id', 'created']
    list_display_links = ['tag']
