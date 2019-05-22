from django.db import models
from accounts.models import UserProfile


# Create your models here.


class BlogMessages(models.Model):
    #  关注、评论、点赞，留言，系统通知
    ITEMS = (
        (1, '关注'),
        (2, '评论'),
        (3, '点赞'),
        (4, '留言'),
        (5, '系统通知'),
    )
    author = models.ForeignKey(UserProfile, related_name='messages', on_delete=models.CASCADE, verbose_name='作者')
    item = models.CharField(max_length=6, choices=ITEMS, default=5, verbose_name='类型')
    body = models.TextField(blank=True, null=True, verbose_name='内容')
    created = models.DateTimeField(auto_now=True, db_index=True, verbose_name='创建时间')

    class Meta:
        db_table = 'blogmessages'
        verbose_name = '站内消息'
        verbose_name_plural = verbose_name
        ordering = ['-created']

    def __str__(self):
        return self.get_item_display()
