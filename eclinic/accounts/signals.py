from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Profile
from clinicians.models import Clinician
from patients.models import Patient


# Create Profile when User is created
@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, **kwargs):
    if created:
        role = getattr(instance, '_role', None)
        if role:
            Profile.objects.create(user=instance, role=role)


# Create Clinician or Patient profile when Profile is created
@receiver(post_save, sender=Profile)
def create_user_role_models(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'clinician' and not hasattr(instance.user, 'clinician'):
            Clinician.objects.create(user=instance.user)

        if instance.role == 'patient' and not hasattr(instance.user, 'patient'):
            Patient.objects.create(user=instance.user)

            
'''
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
'''
