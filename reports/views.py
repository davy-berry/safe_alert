from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from accounts.models import UserProfile
from status_history.models import ReportStatusHistory

from .forms import ReportForm, StatusUpdateForm, ReportCommentForm
from .models import Category, Report, ReportComment
from .risk import calculate_risk_score, calculate_priority

def home(request):
    return render(
        request,
        "reports/home.html",
    )

def about(request):
    return render(
        request,
        "reports/about.html",
    )

# Create your views here.
@login_required
def create_report(request):

    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)

        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.risk_score = calculate_risk_score(report.category)
            report.priority = calculate_priority(report.risk_score)
            report.save()
            messages.success(request, "Report created successfully.")

            return redirect("my_reports")

    else:
        form = ReportForm()

    return render(
        request,
        "reports/create_report.html",
        {"form": form,
         "stadia_api_key": settings.STADIA_API_KEY,}
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

@login_required
def edit_report(request, report_id):

    report = Report.objects.get(
        id=report_id,
        user=request.user
    )

    if request.method == "POST":
        form = ReportForm(
            request.POST,
            request.FILES,
            instance=report
        )

        if form.is_valid():
            report = form.save(commit=False)

            report.risk_score = calculate_risk_score(
                report.category
            )

            report.priority = calculate_priority(
                report.risk_score
            )

            report.save()
            messages.success(request, "Report updated successfully.")
            return redirect("my_reports")

    else:
        form = ReportForm(instance=report)

    return render(
        request,
        "reports/edit_report.html",
        {"form": form, "report": report, "stadia_api_key": settings.STADIA_API_KEY,}
    )

@login_required
def delete_report(request, report_id):

    report = Report.objects.get(
        id=report_id,
        user=request.user
    )

    if request.method == "POST":
        report.delete()

        messages.success(request, "Report deleted successfully.")

        return redirect("my_reports")

    return render(
        request,
        "reports/delete_report.html",
        {
            "report": report,
        }
    )

@login_required
def admin_reports(request):

    if request.user.profile.role != UserProfile.COMMUNITY_ADMIN:
        messages.warning(request, "You do not have permission to access this page.")
        return redirect("my_reports")

    reports = Report.objects.all().order_by("-created_at")

    return render(
        request,
        "reports/admin_reports.html",
        {
            "reports": reports,
            "categories": Category.objects.all().order_by("name"),
        }
    )

@login_required
def report_detail(request, report_id):
    if request.user.profile.role != UserProfile.COMMUNITY_ADMIN:
        return redirect("my_reports")

    report = get_object_or_404(
        Report,
        id=report_id
    )

    return render(
        request,
        "reports/report_detail.html",
        {
            "report": report,
        }
    )

@login_required
def my_report_detail(request, report_id):
    report = get_object_or_404(
        Report,
        id=report_id,
        user=request.user
    )

    return render(
        request,
        "reports/report_detail.html",
        {"report": report}
    )

@login_required
def update_report_status(request, report_id):
    if request.user.profile.role != UserProfile.COMMUNITY_ADMIN:
        return redirect("my_reports")

    report = get_object_or_404(
        Report,
        id=report_id
    )

    if request.method == "POST":
        form = StatusUpdateForm(
            request.POST,
            instance=report
        )

        if form.is_valid():

            previous_status = Report.objects.get(
                id=report.id
            ).status

            new_status = form.cleaned_data["status"]

            if previous_status != new_status:

                ReportStatusHistory.objects.create(
                    report=report,
                    previous_status=previous_status,
                    new_status=new_status,
                    changed_by=request.user
                )

            form.save()
            messages.success(request, "Report status updated successfully.")
            return redirect("admin_reports")

    else:
        form = StatusUpdateForm(
            instance=report
        )

    return render(
        request,
        "reports/update_report_status.html",
        {
            "form": form,
            "report": report,
        }
    )


@login_required
def add_report_comment(request, report_id):
    if request.user.profile.role != UserProfile.COMMUNITY_ADMIN:
        return redirect("my_reports")

    report = get_object_or_404(
        Report,
        id=report_id
    )

    if request.method == "POST":
        form = ReportCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.report = report
            comment.user = request.user
            comment.save()
            messages.success(request, "Comment added successfully.")

            return redirect("admin_reports")

    else:
        form = ReportCommentForm()

    return render(
        request,
        "reports/add_report_comment.html",
        {
            "form": form,
            "report": report,
        }
    )

@login_required
def heatmap(request):
    if request.user.profile.role != UserProfile.COMMUNITY_ADMIN:
        messages.warning(request, "You do not have permission to access this page.")
        return redirect("my_reports")

    reports = Report.objects.exclude(
        latitude__isnull=True
    ).exclude(
        longitude__isnull=True
    )

    return render(
        request,
        "reports/heatmap.html",
        {
            "reports": reports,
            "stadia_api_key": settings.STADIA_API_KEY,
        }
    )