"""Tests covering report access, permissions, and admin workflows.

These tests confirm that authenticated users can create and manage
reports only when allowed, and that admin actions produce the expected
state changes and related records.
"""

from django.test import TestCase
from django.contrib.auth.models import User

from reports.models import Category, Report

from accounts.models import UserProfile

from status_history.models import ReportStatusHistory


class ReportAccessTests(TestCase):
    """Verify report permissions and admin actions for community users."""

    def setUp(self):
        """Create a standard user, profile, category, and report."""
        # Create the test user used throughout the permission checks.
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )

        # Assign a profile so the app can evaluate community permissions.
        UserProfile.objects.create(
            user=self.user,
            role=UserProfile.COMMUNITY_USER,
        )

        # Create a report category for the sample safety report.
        self.category = Category.objects.create(
            name="Road Safety",
            description="Road-related safety issues",
            risk_weight=70,
        )

        # Create the report used by permission and admin workflow tests.
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
        """Ensure unauthenticated users are redirected to login."""
        response = self.client.get("/reports/my_reports/")

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_user_cannot_edit_another_users_report(self):
        """Ensure a user cannot edit a report that belongs to someone else."""
        # Create a second user to act as the unauthorized editor.
        another_user = User.objects.create_user(
            username="anotheruser",
            password="AnotherPassword123!",
        )

        self.client.login(
            username="anotheruser",
            password="AnotherPassword123!",
        )

        response = self.client.get(
            f"/reports/edit/{self.report.id}/",
        )

        self.assertEqual(response.status_code, 404)

    def test_user_cannot_delete_another_users_report(self):
        """Ensure a user cannot delete another user's report."""
        # Create a second user to act as the unauthorized deleter.
        another_user = User.objects.create_user(
            username="deleteuser",
            password="DeletePassword123!",
        )

        self.client.login(
            username="deleteuser",
            password="DeletePassword123!",
        )

        response = self.client.get(
            f"/reports/delete/{self.report.id}/",
        )

        self.assertEqual(response.status_code, 404)

    def test_logged_in_user_can_create_report(self):
        """Allow an authenticated user to submit a new report."""
        self.client.login(
            username="testuser",
            password="TestPassword123!",
        )

        data = {
            "category": self.category.id,
            "title": "Broken street lighting",
            "description": "Several street lights are not working in "
            "this area.",
            "location": "Birmingham",
            "latitude": 52.4862,
            "longitude": -1.8904,
        }

        response = self.client.post(
            "/reports/create/",
            data,
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Report.objects.filter(
                title="Broken street lighting",
                user=self.user,
            ).exists()
        )

    def test_community_user_cannot_access_admin_reports(self):
        """Block community users from the admin report dashboard."""
        self.user.profile.role = "community_user"
        self.user.profile.save()

        self.client.login(
            username="testuser",
            password="TestPassword123!",
        )

        response = self.client.get("/reports/admin/")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/reports/my_reports/")

    def test_community_admin_can_access_admin_reports(self):
        """Allow community admins to view the admin report dashboard."""
        self.user.profile.role = UserProfile.COMMUNITY_ADMIN
        self.user.profile.save()

        self.client.login(
            username="testuser",
            password="TestPassword123!",
        )

        response = self.client.get("/reports/admin/")

        self.assertEqual(response.status_code, 200)

    def test_community_admin_can_update_report_status(self):
        """Verify admins can change a report status through the admin view."""
        self.user.profile.role = UserProfile.COMMUNITY_ADMIN
        self.user.profile.save()

        self.client.login(
            username="testuser",
            password="TestPassword123!",
        )

        response = self.client.post(
            f"/reports/admin/update/{self.report.id}/",
            {"status": "in_progress"},
        )

        self.assertEqual(response.status_code, 302)

        self.report.refresh_from_db()

        self.assertEqual(
            self.report.status,
            "in_progress",
        )

    def test_status_update_creates_status_history(self):
        """Ensure status changes create a history record for auditing."""
        self.user.profile.role = UserProfile.COMMUNITY_ADMIN
        self.user.profile.save()

        self.client.login(
            username="testuser",
            password="TestPassword123!",
        )

        self.client.post(
            f"/reports/admin/update/{self.report.id}/",
            {"status": "in_progress"},
        )

        history = ReportStatusHistory.objects.get(
            report=self.report,
        )

        self.assertEqual(
            history.previous_status,
            "reported",
        )

        self.assertEqual(
            history.new_status,
            "in_progress",
        )

        self.assertEqual(
            history.changed_by,
            self.user,
        )

    def test_community_admin_can_add_comment(self):
        """Verify admins can add a comment to a report."""
        self.user.profile.role = UserProfile.COMMUNITY_ADMIN
        self.user.profile.save()

        self.client.login(
            username="testuser",
            password="TestPassword123!",
        )

        response = self.client.post(
            f"/reports/admin/comment/{self.report.id}/",
            {"comment": "This issue has been reviewed."},
        )

        self.assertEqual(response.status_code, 302)

        comment = self.report.comments.get()

        self.assertEqual(
            comment.comment,
            "This issue has been reviewed.",
        )

        self.assertEqual(
            comment.user,
            self.user,
        )

        self.assertEqual(
            comment.report,
            self.report,
        )
