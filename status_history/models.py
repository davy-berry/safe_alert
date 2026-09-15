from django.db import models
from django.contrib.auth.models import User

from reports.models import Report


class ReportStatusHistory(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name="status_history")

    previous_status = models.CharField(max_length=20, choices=Report.STATUS_CHOICES)

    new_status = models.CharField(max_length=20, choices=Report.STATUS_CHOICES)

    changed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="status_changes")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.report.title}: "
            f"{self.previous_status} → {self.new_status}"
        )