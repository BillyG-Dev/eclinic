from django.contrib import admin
from .models import UserProfile  # <-- fixed

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')

