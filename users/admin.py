from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import Users

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'is_staff', 'is_active', 'is_superuser', 'role')
    search_fields = ('username',)
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','role', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )

admin.site.register(Users, UserAdmin)