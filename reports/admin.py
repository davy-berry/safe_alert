from django.contrib import admin
from .models import Report, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Configure how categories appear and are managed in the admin site."""

    list_display = ('name', 'risk_weight', 'description', 'created_at')
    list_filter = ('risk_weight',)
    search_fields = ('name',)

    def has_module_permission(self, request):
        """Allow only superusers to access this admin module."""
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        """Allow only superusers to view category entries."""
        return request.user.is_superuser

    def has_add_permission(self, request):
        """Allow only superusers to create category entries."""
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        """Allow only superusers to edit category entries."""
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        """Allow only superusers to delete category entries."""
        return request.user.is_superuser


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    """Configure how report records appear in the admin dashboard."""

    list_display = (
        'title',
        'user',
        'category',
        'priority',
        'status',
        'risk_score',
        'created_at',
    )
    list_filter = ('status', 'category', 'priority')
    search_fields = ('title', 'description', 'location', 'user__username')
    readonly_fields = ('risk_score', 'priority', 'created_at', 'updated_at')
