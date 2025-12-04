from django import forms
from .models import Appointment
from clinicians.models import Clinician

class AppointmentForm(forms.ModelForm):
    clinician = forms.ModelChoiceField(queryset=Clinician.objects.filter(duty_status=True))

    class Meta:
        model = Appointment
        fields = ['clinician', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'clinician': forms.Select(attrs={'class': 'form-select'}),
        }
