from django.contrib import admin
from .models import ArticleColumn


# Register your models here.

@admin.register(ArticleColumn)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['user', 'column', 'created']
    list_filter = ['column']
