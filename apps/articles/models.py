from django.db import models
from django.utils import timezone
# 自带不支持中文
# from django.utils.text import slugify
# awesome-slugify 支持中文
from slugify import slugify
from django.urls import reverse
from mdeditor.fields import MDTextField
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
    STATUS = (
        ('1', '公开'),
        ('2', '私密'),
        ('3', '草稿'),
        ('4', '删除'),
    )
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
    # body = models.TextField(verbose_name='内容')

    body = MDTextField(verbose_name='内容')
    slug = models.SlugField(max_length=200, blank=True, null=False, verbose_name='访问地址')
    status = models.CharField(max_length=5, choices=STATUS, default='1', verbose_name='状态')
    allowreply = models.BooleanField(default=True, verbose_name='允许评论')
    top = models.BooleanField(default=False, verbose_name='置顶')
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

    def add_favorite(self, user):
        self.favorites.add(user)
        return self.save()

    def del_favorite(self, user):
        self.favorites.remove(user)
        return self.save()

    def set_top(self):
        self.top = False if self.top else True
        return self.save()

    def set_allowreply(self):
        self.allowreply = False if self.allowreply else True
        return self.save()

    def set_status(self, number):
        if number.isdigit():
            self.status = str(number)
        return self.save()

    def get_absolute_url(self):
        try:
            return reverse("articles:show", args=[self.id, self.slug])
        except Exception as e:
            print(e)
            print(self.id)
            print(self.slug)

    def is_delete(self):
        return self.status == '4'

    def is_draft(self):
        return self.status == '3'

    def is_private(self):
        return self.status == '2'

    def is_public(self):
        return self.status == '1'


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
