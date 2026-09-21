from django.test import TestCase
from django.contrib.auth.models import User

from reports.models import Category, Report


class ReportAccessTests(TestCase):

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

        self.report = Report.objects.create(
            user=self.user,
            category=self.category,
            title="Dangerous road crossing",
            description="This road crossing is dangerous for pedestrians.",
            location="Birmingham",
            latitude=52.4862,
            longitude=-1.8904,
            risk_score=70,
            priority="high",
        )

    def test_my_reports_requires_login(self):
        response = self.client.get("/reports/my_reports/")

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_user_cannot_edit_another_users_report(self):
        another_user = User.objects.create_user(
        username="anotheruser",
        password="AnotherPassword123!"
        )

        self.client.login(
        username="anotheruser",
        password="AnotherPassword123!"
        )

        response = self.client.get(
        f"/reports/edit/{self.report.id}/"
        )

        self.assertEqual(response.status_code, 404)