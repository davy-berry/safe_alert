from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect


def login_required_with_message(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            messages.warning(
                request,
                "You need to be registered and logged in to access this page."
            )
            return redirect("account_login")

        return view_func(request, *args, **kwargs)

    return wrapper