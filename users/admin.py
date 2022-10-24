from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.sessions.models import Session

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_superuser',)
    search_fields = ('username',)
    list_filter = ('groups__name',)
    filter_horizontal = ('groups', 'user_permissions',)

    class Meta:
        model = User


class PermissionAdmin(admin.ModelAdmin):
    search_fields = ('codename',)
    list_display = ('content_type_id', 'id', 'check_permission_name', 'codename',)
    ordering = ('content_type_id', 'id',)

    class Meta:
        model = Permission

    @staticmethod
    def content_type_id(obj):
        """Get permission content type id. """
        return obj.content_type.id

    @staticmethod
    def check_permission_name(obj):
        """Get permission name which is sent as parameter in User.has_perm() method. """
        return f"{obj.content_type.app_label}.{obj.codename}"


admin.site.register(Permission, PermissionAdmin)
admin.site.register(Session)

admin.site.register(User, UserAdmin)
