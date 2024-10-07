from django.contrib import admin
from .models import CustomUser, Role, AdminLogs, Permissions

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'profile_image', 'role_id')
    search_fields = ('username', 'email')
    
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'description')
    search_fields = ('role_name', 'description')
    
class AdminLogsAdmin(admin.ModelAdmin):
    list_display = ('action', 'entity')
    search_fields = ('action',)
    
class PermissionsAdmin(admin.ModelAdmin):
    list_display = ('action', 'entity', 'role')
    search_fields = ('action', 'entity')
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(AdminLogs, AdminLogsAdmin)
admin.site.register(Permissions, PermissionsAdmin)