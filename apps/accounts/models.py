from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext as _

from datetime import datetime


# Create your models here.

# TODO: 用户信息表
class UserProfile(AbstractUser):
    SEXES = (
        ('male', '男'),
        ('female', '女'),
    )
    nick_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='昵称')
    birth = models.DateField(blank=True, null=True, verbose_name='生日')
    phone = models.CharField(max_length=200, blank=True, null=True, unique=True, verbose_name='电话')
    gender = models.CharField(max_length=6, choices=SEXES, default='male', verbose_name='性别')
    profession = models.CharField(max_length=200, blank=True, null=True, verbose_name='职业')
    company = models.CharField(max_length=200, blank=True, null=True, verbose_name='公司')
    school = models.CharField(max_length=200, blank=True, null=True, verbose_name='学校')
    intro = models.TextField(blank=True, null=True, verbose_name='个人简介')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='/static/common/imgs/avatar.png', blank=True,
                              null=True, verbose_name='头像')

    class Meta:
        db_table = 'userprofile'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        ordering = ['-date_joined']

    def __str__(self):
        return _('username') + ':{0}'.format(self.username)

    def age(self):
        return None if not self.birth else round(((datetime.now().date() - self.birth).days) / 365)

    def name(self):
        return self.get_full_name()

    def set_fans(self, fans):
        relationship = UserRelation.objects.get_or_create(focus=self, fans=fans)
        print(relationship)

    def set_unfollow(self, focus):
        relationship = UserRelation.objects.get(focus=focus, fans=self)
        if relationship:
            relationship.delete()
        return True

    def get_fans(self):
        return [relationship.fans for relationship in self.fans.all()]

    def get_focus(self):
        return [relationship.focus for relationship in self.focus.all()]

    age.short_description = '年龄'
    name.short_description = '姓名'
    age = property(age)
    name = property(name)


# TODO: 用户关系表
class UserRelation(models.Model):
    focus = models.ForeignKey(UserProfile, related_name='fans', on_delete=models.CASCADE, verbose_name='关注')
    fans = models.ForeignKey(UserProfile, related_name='focus', on_delete=models.CASCADE, verbose_name='粉丝')

    class Meta:
        db_table = 'userrelation'
        verbose_name = '用户关系'
        verbose_name_plural = verbose_name
        unique_together = ('focus', 'fans')

    def __str__(self):
        return '关注:{0} 粉丝:{1}'.format(self.focus, self.fans)
