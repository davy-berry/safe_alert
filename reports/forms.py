from django import forms
from .models import Report, ReportComment


class ReportForm(forms.ModelForm):
    """Validate report submissions and capture location metadata."""

    description = forms.CharField(max_length=1000, widget=forms.Textarea())

    class Meta:
        """Map the form to the report model and relevant fields."""

        model = Report
        fields = ['category', 'title', 'description',
                  'location', 'latitude', 'longitude', 'image']

        widgets = {
            "latitude": forms.HiddenInput(),
            "longitude": forms.HiddenInput(),
        }

    def clean_title(self):
        """Ensure a report title is long enough to be meaningful."""
        title = self.cleaned_data.get('title', '').strip()
        if len(title) < 5:
            raise forms.ValidationError(
                "Title must be at least 5 characters long.")
        return title

    def clean_description(self):
        """Ensure a report description contains enough detail."""
        description = self.cleaned_data.get('description', '').strip()
        if len(description) < 20:
            raise forms.ValidationError(
                "Description must be at least 10 characters long.")
        return description

    def clean_location(self):
        """Ensure the location field has a useful minimum length."""
        location = self.cleaned_data.get('location', '').strip()
        if len(location) < 3:
            raise forms.ValidationError(
                "Location must be at least 3 characters long.")
        return location

    def clean_latitude(self):
        """Validate latitude values to keep them within valid ranges."""
        latitude = self.cleaned_data.get("latitude")

        if latitude is not None and not -90 <= latitude <= 90:
            raise forms.ValidationError(
                "Latitude must be between -90 and 90."
            )

        return latitude

    def clean_longitude(self):
        """Validate longitude values to keep them within valid ranges."""
        longitude = self.cleaned_data.get("longitude")

        if longitude is not None and not -180 <= longitude <= 180:
            raise forms.ValidationError(
                "Longitude must be between -180 and 180."
            )

        return longitude

    def clean_image(self):
        """Reject images over the allowed file size for report uploads."""
        image = self.cleaned_data.get("image")

        if image and hasattr(image, "size"):
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "Image size must not exceed 5 MB."
                )
        return image


class StatusUpdateForm(forms.ModelForm):
    """Allow the admin to update a report status using a simple form."""

    class Meta:
        """Bind the form to the report model's status field only."""

        model = Report
        fields = ["status"]


class ReportCommentForm(forms.ModelForm):
    """Validate comments that are added to a report update thread."""

    class Meta:
        """Map the form to the report comment model and its field."""

        model = ReportComment
        fields = ["comment"]

        widgets = {
            "comment": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Add an update or comment...",
                }
            )
        }

    def clean_comment(self):
        """Ensure each comment contains enough useful text."""
        comment = self.cleaned_data["comment"].strip()

        if len(comment) < 5:
            raise forms.ValidationError(
                "Please provide at least 5 characters."
            )

        return comment
