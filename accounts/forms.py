from allauth.account.forms import SignupForm, LoginForm
from django.contrib import messages
from .models import UserProfile


class SafeAlertSignupForm(SignupForm):

    def save(self, request):

        user = super().save(request)

        UserProfile.objects.create(
            user=user,
            role=UserProfile.COMMUNITY_USER
        )
        return user


class SafeAlertLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = kwargs.get("request")

        if request and request.GET.get("next"):
            messages.warning(
                request,
                "Please log in or register to access this page."
            )
