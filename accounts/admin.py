from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Configure how user profiles appear in the admin interface."""

    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email')
