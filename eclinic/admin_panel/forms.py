from django import forms
from clinicians.models import Clinician
from patients.models import Patient
from appointments.models import Appointment

class ClinicianForm(forms.ModelForm):
    class Meta:
        model = Clinician
        fields = ['full_name', 'phone_number', 'specialization', 'duty_status']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['full_name', 'phone_number', 'age', 'medical_history']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'clinician', 'date', 'time', 'reason', 'status']
