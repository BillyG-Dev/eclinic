from django.urls import path
from . import views

urlpatterns = [
    path('redirect/', views.dashboard_redirect, name="dashboard_redirect"),

    path('admin/', views.admin_dashboard, name="admin_dashboard"),
    path('clinician/', views.clinician_dashboard, name="clinician_dashboard"),
    path('patient/', views.patient_dashboard, name="patient_dashboard"),
]
