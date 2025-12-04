from django.urls import path
from . import views

urlpatterns = [
    path('clinician/dashboard/', views.clinician_dashboard_view, name='clinician_dashboard'),
    path('toggle-duty/', views.toggle_duty_status, name='toggle_duty_status'),
]
