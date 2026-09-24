from django.test import TestCase
from django.contrib.auth.models import User

from reports.models import Category, Report
from reports.risk import calculate_risk_score, calculate_priority


class ReportRiskPriorityTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

        self.category = Category.objects.create(
            name="Road Safety",
            description="Road-related safety issues",
            risk_weight=70
        )

    def test_risk_score_is_calculated_from_category(self):
        score = calculate_risk_score(self.category)

        self.assertEqual(score, 70)

    def test_priority_is_calculated_from_risk_score(self):
        priority = calculate_priority(70)

        self.assertEqual(priority, "high")

    def test_report_stores_risk_score_and_priority(self):
        risk_score = calculate_risk_score(self.category)
        priority = calculate_priority(risk_score)

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
