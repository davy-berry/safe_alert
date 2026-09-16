from django import forms
from django.contrib.auth.models import User

from allauth.account.forms import SignupForm

from .models import UserProfile


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password",
            "password_confirm",
        ]

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError(
                    "The passwords do not match."
                )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(
            self.cleaned_data["password"]
        )

        if commit:
            user.save()

        return user

class SafeAlertSignupForm(SignupForm):

    def save(self, request):

        user = super().save(request)

        UserProfile.objects.create(
            user=user,
            role=UserProfile.COMMUNITY_USER
        )

        return user