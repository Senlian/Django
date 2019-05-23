from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from accounts.models import UserProfile


# Create your models here.

# TODO: 文章栏目
class ArticleColumns(models.Model):
    author = models.ForeignKey(UserProfile, related_name='columns', on_delete=models.CASCADE, verbose_name='作者')
    body = models.CharField(max_length=200, verbose_name='栏目')
    # created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'articlecolumns'
        verbose_name = '栏目信息'
        verbose_name_plural = verbose_name
        ordering = ['-update']

    def __str__(self):
        return self.body


# TODO: 文章标签
class ArticleTags(models.Model):
    author = models.ForeignKey(UserProfile, related_name='tags', on_delete=models.CASCADE, verbose_name='作者')
    body = models.CharField(max_length=200, verbose_name='关键字')
    # created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'articletags'
        verbose_name = '关键字'
        verbose_name_plural = verbose_name
        unique_together = ('author', 'body')
        ordering = ['-update']

    def __str__(self):
        return self.body


# TODO: 文章信息
class Articles(models.Model):
    author = models.ForeignKey(UserProfile, related_name='articles', on_delete=models.CASCADE, verbose_name='作者')
    column = models.ForeignKey(ArticleColumns, related_name='articles', default=None, on_delete=models.DO_NOTHING,
                               blank=True, null=True, verbose_name='栏目')

    tags = models.ManyToManyField(ArticleTags, related_name='article_tags', default=None, blank=True,
                                  verbose_name='标签')
    likes = models.ManyToManyField(UserProfile, related_name='article_likes', default=None, blank=True,
                                   verbose_name='点赞')
    favorites = models.ManyToManyField(UserProfile, related_name='article_favorites', default=None, blank=True,
                                       verbose_name='收藏')

    title = models.CharField(max_length=200, verbose_name='标题')
    body = models.TextField(verbose_name='内容')
    slug = models.SlugField(max_length=200, blank=True, null=False, verbose_name='访问地址')
    # created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'articles'
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name
        ordering = ['-update']
        index_together = [('id', 'slug')]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Articles, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article:article_detail", args=[self.id, self.slug])


# TODO: 文章评论
class ArticleComments(models.Model):
    author = models.ForeignKey(UserProfile, related_name='comments', to_field='username',
                               on_delete=models.SET('未知用户'), verbose_name='作者')
    article = models.ForeignKey(Articles, related_name='comments', on_delete=models.CASCADE, verbose_name='文章')
    body = models.TextField(verbose_name='内容')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'articlecomments'
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name
        ordering = ['-created']
