from django.shortcuts import render
from accounts.decorators import patient_required, clinician_required
from clinicians.models import Clinician
from patients.models import Patient
from appointments.models import Appointment


@patient_required
def patient_dashboard(request):
    patient = Patient.objects.get(user=request.user)
    context = {'patient': patient}
    return render(request, 'patient_dashboard.html', context)


@clinician_required
def clinician_dashboard(request):
    clinician = Clinician.objects.get(user=request.user)
    context = {'clinician': clinician}
    return render(request, 'dashboard/clinician_dashboard.html', context)



def admin_dashboard(request):
    context = {
        "total_patients": Patient.objects.count(),
        "total_clinicians": Clinician.objects.count(),
        "total_appointments": Appointment.objects.count(),
        "active_appointments": Appointment.objects.filter(status="Pending").count(),
    }
    return render(request, "admin_panel/admin_dashboard.html", context)