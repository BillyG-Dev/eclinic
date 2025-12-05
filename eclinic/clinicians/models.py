from django.db import models
from django.contrib.auth.models import User

class Clinician(models.Model):
    SPECIALIZATION_CHOICES = [
        ('General Medicine', 'General Medicine'),
        ('Pediatrics', 'Pediatrics'),
        ('Dermatology', 'Dermatology'),
        ('Gynecology', 'Gynecology'),
        ('Cardiology', 'Cardiology'),
        ('Orthopedics', 'Orthopedics'),
        ('Neurology', 'Neurology'),
        ('Psychiatry', 'Psychiatry'),
        ('Dentistry', 'Dentistry'),
    ]

    DUTY_STATUS = [
        ('On Duty', 'On Duty'),
        ('Off Duty', 'Off Duty'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, default='unknown clinician')
    phone_number = models.CharField(max_length=20, blank=True)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    duty_status = models.CharField(max_length=20, choices=DUTY_STATUS, default='Off Duty')

    def __str__(self):
        return f"{self.full_name} - {self.specialization}"
