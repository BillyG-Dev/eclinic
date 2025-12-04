from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from .models import Patient
from appointments.models import Appointment
from django.utils.timezone import now


@login_required
def patient_dashboard_view(request):
    patient = Patient.objects.get(user=request.user)
    appointments = Appointment.objects.filter(patient=patient).order_by('-date', '-time')

    return render(request, "patients/patient_dashboard.html", {
        "patient": patient,
        "appointments": appointments,
    })

# Create your views here.
