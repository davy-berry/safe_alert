from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    COMMUNITY_USER = 'community_user'
    COMMUNITY_ADMIN = 'community_admin'

    ROLE_CHOICES = [
        (COMMUNITY_USER, 'Community User'),
        (COMMUNITY_ADMIN, 'Community Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=COMMUNITY_USER)

    def __str__(self): 
        return f"{self.user.username} - {self.get_role_display()}"
