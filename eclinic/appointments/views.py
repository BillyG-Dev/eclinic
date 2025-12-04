from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm
from patients.models import Patient
from clinicians.models import Clinician

# Create your views here.
@login_required
def appointment_list_view(request):
    if hasattr(request.user, 'patient'):
        appointments = Appointment.objects.filter(patient=request.user.patient)
    elif hasattr(request.user, 'clinician'):
        appointments = Appointment.objects.filter(clinician=request.user.clinician)
    else:
        appointments = Appointment.objects.none()
    return render(request, "appointments/appointment_list.html", {"appointments": appointments})

@login_required
def appointment_create_view(request):
    if not hasattr(request.user, 'patient'):
        return redirect('clinician_dashboard')  # Only patients can create
    patient = request.user.patient
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, "appointments/appointment_form.html", {"form": form})

@login_required
def appointment_cancel_view(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if hasattr(request.user, 'patient') and appointment.patient == request.user.patient:
        appointment.status = 'cancelled'
        appointment.save()
    return redirect('appointment_list')
