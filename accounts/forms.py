from allauth.account.forms import SignupForm, LoginForm
from django.contrib import messages
from .models import UserProfile


class SafeAlertSignupForm(SignupForm):
    """Create a local user profile when a new account is registered."""

    def save(self, request):
        """Create the user and attach the default community user role."""
        user = super().save(request)

        UserProfile.objects.create(
            user=user,
            role=UserProfile.COMMUNITY_USER,
        )
        return user


class SafeAlertLoginForm(LoginForm):
    """Show a warning when a user must sign in before accessing a page."""

    def __init__(self, *args, **kwargs):
        """Set up the login form and display a message for protected pages."""
        super().__init__(*args, **kwargs)

        request = kwargs.get("request")

        if request and request.GET.get("next"):
            messages.warning(
                request,
                "Please log in or register to access this page.",
            )
