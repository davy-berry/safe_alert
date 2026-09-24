"""Model definitions for reporting and reviewing safety incidents."""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """Represent a report category used to classify safety issues."""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    risk_weight = models.PositiveIntegerField(default=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the category name as the model string value."""
        return self.name


class Report(models.Model):
    """Represent a submitted safety report and its current status."""

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
    latitude = models.DecimalField(
        max_digits=10, decimal_places=6, blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=10, decimal_places=6, blank=True, null=True
    )
    image = CloudinaryField("image", blank=True, null=True)
    risk_score = models.PositiveIntegerField(default=0)
    priority = models.CharField(
        max_length=20, choices=PRIORITY_CHOICES, default="low"
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=REPORTED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Define model-level constraints for report risk scores."""

        constraints = [
            models.CheckConstraint(
                condition=models.Q(risk_score__gte=0)
                & models.Q(risk_score__lte=100),
                name="risk_score_between_0_and_100",
            ),
        ]

    def __str__(self):
        """Return the report title as the model string value."""
        return self.title


class ReportComment(models.Model):
    """Store a user comment associated with a report."""

    report = models.ForeignKey(
        Report, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="report_comments"
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a readable label for the comment."""
        return f"Comment on {self.report.title} by {self.user.username}"
