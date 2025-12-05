from django.contrib import admin
from .models import Patient
# Register your models here.

#admin.site.register(Patient)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number','full_name', 'age')
    search_fields = ('user__username',)