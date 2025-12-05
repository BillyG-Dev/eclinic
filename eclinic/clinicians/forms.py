from django import forms
from .models import Clinician

class ClinicianForm(forms.ModelForm):
    class Meta:
        model = Clinician
        fields = ['full_name', 'phone_number', 'specialization', 'duty_status']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.Select(attrs={'class': 'form-select'}),
            'duty_status': forms.Select(attrs={'class': 'form-select'}),
        }
