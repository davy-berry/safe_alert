from django import forms
from .models import Report, ReportComment

class ReportForm(forms.ModelForm):

    description = forms.CharField(max_length=1000, widget=forms.Textarea())

    class Meta:
        model = Report
        fields = ['category', 'title', 'description', 'location', 'latitude', 'longitude', 'image']

        widgets = {
            "latitude": forms.HiddenInput(),
            "longitude": forms.HiddenInput(),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description', '').strip()
        if len(description) < 20:
            raise forms.ValidationError("Description must be at least 10 characters long.")
        return description

    def clean_location(self):
        location = self.cleaned_data.get('location', '').strip()
        if len(location) < 3:
            raise forms.ValidationError("Location must be at least 3 characters long.")
        return location

    def clean_latitude(self):
        latitude = self.cleaned_data.get("latitude")

        if latitude is not None and not -90 <= latitude <= 90:
            raise forms.ValidationError("Latitude must be between -90 and 90.")

        return latitude

    def clean_longitude(self):
        longitude = self.cleaned_data.get("longitude")

        if longitude is not None and not -180 <= longitude <= 180:
            raise forms.ValidationError("Longitude must be between -180 and 180.")

        return longitude

    def clean_image(self):
        image = self.cleaned_data.get("image")

        if image and hasattr(image, "size"):
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Image size must not exceed 5 MB.")
        return image
    

class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["status"] 

class ReportCommentForm(forms.ModelForm):
    class Meta:
        model = ReportComment
        fields = ["comment"]

        widgets = {
            "comment": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Add an update or comment..."}
            )
        }

    def clean_comment(self):
        comment = self.cleaned_data["comment"].strip()

        if len(comment) < 5:
            raise forms.ValidationError("Please provide at least 5 characters.")

        return comment

    