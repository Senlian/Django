from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class UserInfoHandler(models.Model):
    # blank=False,表示必填
    # unique=True,表示唯一
    uid = models.CharField(verbose_name='账号', max_length=128, blank=False, unique=True)
    pwd = models.CharField(verbose_name='密码', max_length=256, blank=False)

    name = models.CharField(verbose_name='姓名', max_length=128, blank=True)
    phone = models.CharField(verbose_name='电话号码', max_length=15, blank=True, unique=True, null=True,
                             validators=(RegexValidator(regex=r'^(86)?(\-)?1\d{10}$', message='请输入正确的电话号码'),))
    email = models.EmailField(verbose_name='邮箱', blank=True, unique=True, null=True)

    limits = models.PositiveIntegerField(verbose_name='权限', default=0)

    ctime = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    mtime = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'WebRedis_UserInfo'
        verbose_name_plural = '用户列表'
        verbose_name = '用户'
    def __str__(self):
        return self.uid


class RedisHandler(models.Model):
    host = models.GenericIPAddressField(verbose_name='IP地址', blank=False)
    port = models.PositiveIntegerField(
            verbose_name='端口号',
            blank=False,
            validators=(RegexValidator(regex=r'(^6[0-5]{2}[0-3][0-5]$)|(^[0-5][0-9]{4}$)|(^[1-9][0-9]{0,3}$)',
                                       message='端口号为1~65536间的数字', code="c1"),
                        ), error_messages={'c1': '端口号为1~65536间的数字'})
    name = models.CharField(verbose_name='服务器名', max_length=128, blank=False, unique=True)
    user = models.CharField(verbose_name='用户名', blank=True, max_length=128)
    pwd = models.CharField(verbose_name='密码', blank=True, max_length=256)

    status = models.BooleanField(verbose_name='状态', default=False)
    count = models.PositiveIntegerField(verbose_name='数据量', default=0)

    uid = models.ForeignKey(verbose_name='添加人', to=UserInfoHandler, on_delete=models.CASCADE)
    describtion = models.TextField(verbose_name='描述', max_length=512, blank=True)

    ctime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    mtime = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'WebRedis_RedisList'
        verbose_name_plural = '数据服列表'
        verbose_name = '数据服'

        unique_together = ('host', 'port')

    def __str__(self):
        return str(self.host) + ':' + str(self.port)

    def color_set(self):
        if self.status:
            color = 'blue'
            value = '正常'
        else:
            color = 'red'
            value = '异常'
        from django.utils.html import format_html
        format_html('<span style="color: {};">{}</span>', color, value)

    color_set.short_description = status.verbose_name
