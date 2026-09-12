from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report
from .risk import calculate_risk_score, calculate_priority


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

            return redirect("my_reports")

    else:
        form = ReportForm(instance=report)

    return render(
        request,
        "reports/edit_report.html",
        {
            "form": form,
            "report": report,
        }
    )
