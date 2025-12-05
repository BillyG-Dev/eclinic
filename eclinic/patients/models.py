from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, default='unknown patient')
    phone_number = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(null=True, blank=True)
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return self.full_name
