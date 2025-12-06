from django.urls import path
from . import views


urlpatterns = [
    path('patient/', views.patient_dashboard, name='patient_dashboard'),
    path('clinician/', views.clinician_dashboard, name='clinician_dashboard'),
]
