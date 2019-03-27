from django.contrib import admin
from .models import AccountUserProfileModel, AccountUserDetailModel

# Register your models here.
@admin.register(AccountUserProfileModel)
class AccountUserProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'age', 'birth', 'sex', 'photo', 'created']
    list_display_links = ['age', 'birth', 'sex']


@admin.register(AccountUserDetailModel)
class AccountUserDetailModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'phone', 'profession', 'company', 'school', 'intro']
    list_display_links = ['phone', 'profession', 'company', 'school', 'intro']
