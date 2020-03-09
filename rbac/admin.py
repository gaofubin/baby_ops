from django.contrib import admin
from .models import UserProfile, Role, Permission, Menu
from django.contrib.auth.admin import UserAdmin


class UserInfoAdmin(UserAdmin):
    # 重写fieldsets在admin后台加入自己新增的字段
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('name', 'email', 'roles', 'image')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )


admin.site.register(UserProfile, UserInfoAdmin)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Menu)
