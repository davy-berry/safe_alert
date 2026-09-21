from django.test import TestCase
from django.contrib.auth.models import User

from reports.models import Category, Report

from accounts.models import UserProfile


class ReportAccessTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

        UserProfile.objects.create(
            user=self.user,
            role=UserProfile.COMMUNITY_USER
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


    def test_user_cannot_delete_another_users_report(self):
        another_user = User.objects.create_user(
        username="deleteuser",
        password="DeletePassword123!"
        )

        self.client.login(
        username="deleteuser",
        password="DeletePassword123!"
        )

        response = self.client.get(
        f"/reports/delete/{self.report.id}/"
        )

        self.assertEqual(response.status_code, 404)

    def test_logged_in_user_can_create_report(self):
        self.client.login(
        username="testuser",
        password="TestPassword123!"
        )

        data = {
        "category": self.category.id,
        "title": "Broken street lighting",
        "description": "Several street lights are not working in this area.",
        "location": "Birmingham",
        "latitude": 52.4862,
        "longitude": -1.8904,
        }

        response = self.client.post(
        "/reports/create/",
        data
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
        Report.objects.filter(
            title="Broken street lighting",
            user=self.user
        ).exists()
        )

    def test_community_user_cannot_access_admin_reports(self):
        self.user.profile.role = "community_user"
        self.user.profile.save()

        self.client.login(
            username="testuser",
            password="TestPassword123!"
        )

        response = self.client.get("/reports/admin/")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/reports/my_reports/")

    def test_community_admin_can_access_admin_reports(self):
        self.user.profile.role = UserProfile.COMMUNITY_ADMIN
        self.user.profile.save()

        self.client.login(
            username="testuser",
            password="TestPassword123!"
        )

        response = self.client.get("/reports/admin/")

        self.assertEqual(response.status_code, 200)