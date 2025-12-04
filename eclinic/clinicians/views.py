from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Clinician

# -------------------------
# CLINICIAN DASHBOARD
# -------------------------
@login_required
def clinician_dashboard_view(request):
    try:
        clinician = request.user.clinician
    except Clinician.DoesNotExist:
        messages.error(request, "Clinician profile not found.")
        return redirect('dashboard')

    context = {
        'clinician': clinician
    }
    return render(request, 'clinicians/clinician_dashboard.html', context)


# -------------------------
# TOGGLE DUTY STATUS
# -------------------------
@login_required
def toggle_duty_status(request):
    try:
        clinician = request.user.clinician
    except Clinician.DoesNotExist:
        messages.error(request, "Clinician profile not found.")
        return redirect('dashboard')

    clinician.duty_status = not clinician.duty_status
    clinician.save()
    messages.success(request, f"Duty status updated to {'On Duty' if clinician.duty_status else 'Off Duty'}")
    return redirect('clinician_dashboard')
