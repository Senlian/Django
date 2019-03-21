from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from slugify import slugify
from mdeditor.fields import MDTextField


# Create your models here.
class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='article_column', on_delete=models.DO_NOTHING)
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column

    class Meta:
        unique_together = ('user', 'column')
        verbose_name = "栏目信息"
        verbose_name_plural = verbose_name

class ArticleTag(models.Model):
    author = models.ForeignKey(User, related_name='tag', on_delete=models.DO_NOTHING)
    tag = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = '关键字'
        verbose_name_plural = verbose_name

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='article')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    column = models.ForeignKey(ArticleColumn, on_delete=models.DO_NOTHING, related_name='article_column')
    # body = models.TextField()
    body = MDTextField()
    created = models.DateTimeField(default=timezone.now())
    update = models.DateTimeField(auto_now=True)
    user_like = models.ManyToManyField(User, related_name='articles_like', blank=True)
    article_tag = models.ManyToManyField(ArticleTag, related_name='article_tag', blank=True)

    class Meta:
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name
        ordering = ['-update']
        index_together = [('id', 'slug')]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(ArticlePost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article:article_detail", args=[self.id, self.slug])


class ArticleComments(models.Model):
    author = models.ForeignKey(User, related_name='comments', to_field='username', on_delete=models.DO_NOTHING)
    article = models.ForeignKey(ArticlePost, related_name='comments', on_delete=models.DO_NOTHING)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '访客评论'
        verbose_name_plural = verbose_name
        ordering = ['-created']



