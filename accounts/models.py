"""User profile model for role-based account access and permissions."""

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Store a user's role and related access permissions."""

    COMMUNITY_USER = 'community_user'
    COMMUNITY_ADMIN = 'community_admin'

    ROLE_CHOICES = [
        (COMMUNITY_USER, 'Community User'),
        (COMMUNITY_ADMIN, 'Community Admin'),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default=COMMUNITY_USER)

    def __str__(self):
        """Return a readable display string for the user profile."""
        return f"{self.user.username} - {self.get_role_display()}"
