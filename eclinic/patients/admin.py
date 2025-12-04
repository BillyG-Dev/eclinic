from django.contrib import admin
from .models import Patient
# Register your models here.

#admin.site.register(Patient)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'medical_history', 'date_of_birth')
    search_fields = ('user__username',)