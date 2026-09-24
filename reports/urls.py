from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_report, name='create_report'),
    path('my_reports/', views.my_reports, name='my_reports'),
    path('edit/<int:report_id>/', views.edit_report, name='edit_report'),
    path('delete/<int:report_id>/', views.delete_report, name='delete_report'),

    path('admin/', views.admin_reports, name='admin_reports'),
    path("admin/report/<int:report_id>/",
         views.report_detail, name="report_detail",),
    path("my_reports/<int:report_id>/",
         views.my_report_detail, name="my_report_detail"),
    path('admin/update/<int:report_id>/',
         views.update_report_status, name='update_report_status'),
    path("admin/comment/<int:report_id>/",
         views.add_report_comment, name="add_report_comment",),

    path("heatmap/", views.heatmap, name="heatmap"),
]
