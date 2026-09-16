from allauth.account.forms import SignupForm
from .models import UserProfile

class SafeAlertSignupForm(SignupForm):

    def save(self, request):

        user = super().save(request)

        UserProfile.objects.create(
            user=user,
            role=UserProfile.COMMUNITY_USER
        )

        return user