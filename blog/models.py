from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from mdeditor.fields import MDTextField

# Create your models here.

class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name="blog_posts", on_delete=models.DO_NOTHING)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '博客列表'
        verbose_name_plural = verbose_name
        ordering = ('publish',)

    def __str__(self):
        return self.title
