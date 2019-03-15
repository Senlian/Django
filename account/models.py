from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "基本信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'user {0}'.format(self.user.username)


class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    school = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True)
    photo = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = "详细信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'user {0}'.format(self.user.username)
