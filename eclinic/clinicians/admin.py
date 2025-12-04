from django.contrib import admin
from .models import Clinician

#admin.site.register(Clinician)
@admin.register(Clinician)
class ClinicianAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'duty_status')
    list_filter = ('specialization', 'duty_status')
    search_fields = ('user__username', 'specialization')
