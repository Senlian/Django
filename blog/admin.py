from django.contrib import admin
from .models import BlogArticles


# Register your models here.
@admin.register(BlogArticles)
class BlogArticlesHandler(admin.ModelAdmin):
    list_display = ['title', 'author', 'body', 'publish']
    list_display_links = ['title', 'body']
    list_filter = ['publish', 'author']
    search_fields = ('title', 'author__username')
    ordering = ['-publish']
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    list_per_page = 2
