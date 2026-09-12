from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report


# Create your views here.
@login_required
def create_report(request):

    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)

        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()

            return redirect("my_reports")

    else:
        form = ReportForm()

    return render(
        request,
        "reports/create_report.html",
        {"form": form}
    )

@login_required
def my_reports(request):

    reports = Report.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "reports/my_reports.html",
        {"reports": reports}
    )