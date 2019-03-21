from django.contrib import admin
from .models import UserProfile, UserInfo


# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'phone', 'birth']


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['school', 'company', 'profession', 'address', 'aboutme', 'photo']
    list_filter = ['school', 'company', 'profession']
