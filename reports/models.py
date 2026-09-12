from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """Represents a report category used to classify safety issues."""
    
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    risk_weight = models.PositiveIntegerField(default=50)   #represents the risk associated with a category
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Report(models.Model):
    """Stores a public safety issue reported by a user and tracked through review.

    Each report includes the reporter, issue category, location, description,
    and a lifecycle status from submission through resolution.
    """

    # Status choices
    REPORTED = "reported"
    UNDER_REVIEW = "under_review"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CONFIRMED = "confirmed"
    REJECTED = "rejected"

    STATUS_CHOICES = [
        (REPORTED, "Reported"),
        (UNDER_REVIEW, "Under Review"),
        (IN_PROGRESS, "In Progress"),
        (RESOLVED, "Resolved"),
        (CONFIRMED, "Confirmed"),
        (REJECTED, "Rejected"),
    ]

    PRIORITY_CHOICES = [
    ("low", "Low"),
    ("medium", "Medium"),
    ("high", "High"),
    ("critical", "Critical"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    image = models.ImageField(upload_to='reports/', blank=True, null=True)
    risk_score = models.PositiveIntegerField(default=0)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=REPORTED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition = models.Q(risk_score__gte=0) &
                      models.Q(risk_score__lte=100),
                name="risk_score_between_0_and_100",
            ),
        ]

    def __str__(self):
        return self.title