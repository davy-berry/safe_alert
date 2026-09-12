from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_report, name='create_report'),
    path('my_reports/', views.my_reports, name='my_reports'),
]