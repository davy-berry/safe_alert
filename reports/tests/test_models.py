"""Tests for the report risk and priority calculation workflow."""

from django.test import TestCase
from django.contrib.auth.models import User

from reports.models import Category, Report
from reports.risk import calculate_risk_score, calculate_priority


class ReportRiskPriorityTests(TestCase):
    """Check that report risk and priority values are calculated correctly."""

    def setUp(self):
        """Create the shared user and category data for all test cases."""
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

        # Use one category with a known risk weight for all calculations.
        self.category = Category.objects.create(
            name="Road Safety",
            description="Road-related safety issues",
            risk_weight=70
        )

    def test_risk_score_is_calculated_from_category(self):
        """Verify that the category risk weight is used for the risk score."""
        score = calculate_risk_score(self.category)

        self.assertEqual(score, 70)

    def test_priority_is_calculated_from_risk_score(self):
        """Verify that a risk score maps to the expected priority label."""
        priority = calculate_priority(70)

        self.assertEqual(priority, "high")

    def test_report_stores_risk_score_and_priority(self):
        """Verify that created reports save the calculated values."""
        risk_score = calculate_risk_score(self.category)
        priority = calculate_priority(risk_score)

        # Build a report using the calculated score and priority values.
        report = Report.objects.create(
            user=self.user,
            category=self.category,
            title="Dangerous road crossing",
            description="This road crossing is dangerous for pedestrians.",
            location="Birmingham",
            risk_score=risk_score,
            priority=priority,
        )

        self.assertEqual(report.risk_score, 70)
        self.assertEqual(report.priority, "high")
