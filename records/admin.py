from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from records.models import GoUser, GoCustomerRegistration


class GoUserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_superuser')
    search_fields = ('email', 'username', 'phone')
    filter_horizontal = ()
    list_filter = ('last_login', 'is_active')
    fieldsets = ()

    ordering = ('username', 'email', 'date_joined', 'is_admin', 'is_active', 'is_superuser')
    # 119175013Steve
    add_fieldsets = [
        (
            None, {
                'classes': 'wide',
                'fields': ('username', 'email', 'phone', 'password1', 'password2')
            },
        )
    ]

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True


class MyAdminSite(AdminSite):
    site_header = 'Go Immigration administration'


admin.site.register(GoUser, GoUserAdmin)
admin.site.unregister(Group)
admin.site.register(GoCustomerRegistration)
