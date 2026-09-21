from django.test import TestCase
from django.contrib.auth.models import User

from reports.models import Category
from reports.forms import ReportForm


class ReportFormTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Road Safety",
            description="Road-related safety issues",
            risk_weight=70
        )

        self.valid_data = {
            "category": self.category.id,
            "title": "Dangerous road crossing",
            "description": "This road crossing is dangerous for pedestrians.",
            "location": "Birmingham",
            "latitude": 52.4862,
            "longitude": -1.8904,
        }

    def test_valid_report_form(self):
        form = ReportForm(data=self.valid_data)

        self.assertTrue(form.is_valid())

    def test_title_too_short(self):
        data = self.valid_data.copy()
        data["title"] = "Road"

        form = ReportForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_description_too_short(self):
        data = self.valid_data.copy()
        data["description"] = "Too short"

        form = ReportForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn("description", form.errors)

    def test_location_too_short(self):
        data = self.valid_data.copy()
        data["location"] = "UK"

        form = ReportForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn("location", form.errors)

    def test_invalid_latitude(self):
        data = self.valid_data.copy()
        data["latitude"] = 100

        form = ReportForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn("latitude", form.errors)

    def test_invalid_longitude(self):
        data = self.valid_data.copy()
        data["longitude"] = 200

        form = ReportForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn("longitude", form.errors)