from django.contrib import admin
from .models import Appointment

# Register your models here.
#admin.site.register(Appointment)
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'clinician', 'date', 'time', 'status')
    list_filter = ('status', 'date')
    search_fields = ('patient__user__username', 'clinician__user__username')