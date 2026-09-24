"""Tests for validating report and comment form inputs."""

from django.test import TestCase
from django.contrib.auth.models import User

from reports.models import Category
from reports.forms import ReportForm, ReportCommentForm


class ReportFormTests(TestCase):
    """Check that the report and comment forms enforce expected rules."""

    def setUp(self):
        """Create category data and valid report values for all tests."""
        self.category = Category.objects.create(
            name="Road Safety",
            description="Road-related safety issues",
            risk_weight=70
        )

        # Store a valid payload that each validation test can copy and adjust.
        self.valid_data = {
            "category": self.category.id,
            "title": "Dangerous road crossing",
            "description": "This road crossing is dangerous for pedestrians.",
            "location": "Birmingham",
            "latitude": 52.4862,
            "longitude": -1.8904,
        }

    def test_valid_report_form(self):
        """Verify that a complete valid report payload passes validation."""
        form = ReportForm(data=self.valid_data)

        self.assertTrue(form.is_valid())

    def test_title_too_short(self):
        """Ensure short titles are rejected by the report form."""
        data = self.valid_data.copy()
        data["title"] = "Road"

        form = ReportForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_description_too_short(self):
        """Ensure short descriptions are rejected by the report form."""
        data = self.valid_data.copy()
        data["description"] = "Too short"

        form = ReportForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn("description", form.errors)

    def test_location_too_short(self):
        """Ensure short locations are rejected by the report form."""
        data = self.valid_data.copy()
        data["location"] = "UK"

        form = ReportForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn("location", form.errors)

    def test_invalid_latitude(self):
        """Ensure latitude values outside the valid range are rejected."""
        data = self.valid_data.copy()
        data["latitude"] = 100

        form = ReportForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn("latitude", form.errors)

    def test_invalid_longitude(self):
        """Ensure longitude values outside the valid range are rejected."""
        data = self.valid_data.copy()
        data["longitude"] = 200

        form = ReportForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn("longitude", form.errors)

    def test_comment_too_short(self):
        """Ensure comments below the minimum length are rejected."""
        from reports.forms import ReportCommentForm

        form = ReportCommentForm(
            data={"comment": "Hi"}
        )

        self.assertFalse(form.is_valid())
        self.assertIn("comment", form.errors)
