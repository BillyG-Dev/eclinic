from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from patients.models import Patient
from clinicians.models import Clinician
from appointments.models import Appointment


# -------------------------
# DASHBOARD REDIRECT BASED ON ROLE
# -------------------------
@login_required
def dashboard_redirect(request):
    try:
        role = request.user.profile.role

        if role == "admin":
            return redirect('admin_dashboard')
        elif role == "clinician":
            return redirect('clinician_dashboard')
        elif role == "patient":
            return redirect('patient_dashboard')
        else:
            messages.error(request, "Invalid role assigned.")
            return redirect('login')
    except:
        messages.error(request, "Profile not found. Please contact admin.")
        return redirect('login')


# -------------------------
# ADMIN DASHBOARD
# -------------------------
@login_required
def admin_dashboard(request):
    # Ensure only admin/superuser access this
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, "You do not have permission to access the admin dashboard.")
        return redirect('login')

    patients = Patient.objects.all()
    clinicians = Clinician.objects.all()
    appointments = Appointment.objects.all().order_by('-date', '-time')

    context = {
        "patients": patients,
        "clinicians": clinicians,
        "appointments": appointments,
    }
    return render(request, "dashboard/admin_dashboard.html", context)


# -------------------------
# CLINICIAN DASHBOARD
# -------------------------
@login_required
def clinician_dashboard(request):
    """Clinician dashboard showing their info and appointments"""
    try:
        clinician = request.user.clinician
    except Clinician.DoesNotExist:
        messages.error(request, "Clinician profile not found.")
        return redirect("login")

    appointments = Appointment.objects.filter(clinician=clinician).order_by('date', 'time')

    context = {
        "clinician": clinician,
        "appointments": appointments,
    }
    return render(request, "dashboard/clinician_dashboard.html", context)


# -------------------------
# PATIENT DASHBOARD
# -------------------------
@login_required
def patient_dashboard(request):
    """Patient dashboard showing profile and appointments"""
    try:
        patient = request.user.patient
    except Patient.DoesNotExist:
        messages.error(request, "Patient profile not found.")
        return redirect("login")

    appointments = Appointment.objects.filter(patient=patient).order_by('date', 'time')

    context = {
        "patient": patient,
        "appointments": appointments,
    }
    return render(request, "dashboard/patient_dashboard.html", context)