from django.contrib import admin
from .models import Report, Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'risk_weight', 'description', 'created_at')
    list_filter = ('risk_weight',)
    search_fields = ('name',)

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'priority',
                    'status', 'risk_score', 'created_at')
    list_filter = ('status', 'category', 'priority')
    search_fields = ('title', 'description', 'location', 'user__username')
    readonly_fields = ('risk_score', 'priority', 'created_at', 'updated_at')
