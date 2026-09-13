from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import RegistrationForm
from .models import UserProfile


def register(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            UserProfile.objects.create(
                user=user,
                role="community_member"
            )

            login(request, user)

            return redirect("my_reports")

    else:
        form = RegistrationForm()

    return render(
        request,
        "registration/register.html",
        {
            "form": form,
        }
    )
