from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class AccountUserProfileModel(models.Model):
    SEXES = (
        ('male', '男'),
        ('female', '女')
    )
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, verbose_name='账户')
    age = models.IntegerField(blank=True, null=True, verbose_name='年龄')
    birth = models.DateField(blank=True, null=True, verbose_name='生日')

    sex = models.CharField(max_length=10, choices=SEXES, default='male', verbose_name='性别')
    # 上传到MEDIA_ROOT路径下的photos/%Y/%m/%d文件夹
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True, verbose_name='头像')
    created = models.DateTimeField(auto_now_add=timezone.now(), verbose_name='注册日期')

    class Meta:
        verbose_name = '基本资料'
        verbose_name_plural = verbose_name
        ordering = ['-created']

    def __str__(self):
        return 'UserName:{0}'.format(self.user.username)

    #  自定义非模型字段方法，返回显示内容
    def user_display(self):
        return self.user.username

    # 自定义非模型字段方法的标题
    user_display.short_description = '账号'
    # 自定义非模型字段方法不支持排序，需要定义排序依据的字段，减号表示倒序
    user_display.admin_order_field = 'user_id'

    username = property(user_display)


class AccountUserDetailModel(models.Model):
    # 如果不用引号，则绑定模板需要在该模型前定义
    user = models.OneToOneField('AccountUserProfileModel', related_name='user_detail', unique=True,
                                on_delete=models.CASCADE, verbose_name='账户')
    phone = models.CharField(max_length=200, blank=True, null=True, verbose_name='电话')
    profession = models.CharField(max_length=200, blank=True, null=True, verbose_name='职业')
    company = models.CharField(max_length=200, blank=True, null=True, verbose_name='公司')
    school = models.CharField(max_length=200, blank=True, null=True, verbose_name='学校')
    intro = models.TextField(blank=True, null=True, verbose_name='个人简介')

    class Meta:
        verbose_name = '详细资料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'UserName:{0}'.format(self.user.user_id)

    def user_display(self):
        return self.user.user.username

    user_display.short_description = '账号'
    username = property(user_display)

    def email_display(self):
        return self.user.user.email

    email_display.short_description = '邮箱'
    email = property(email_display)