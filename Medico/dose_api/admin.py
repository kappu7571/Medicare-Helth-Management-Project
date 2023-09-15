from django.contrib import admin
from .models import Medication, Reminder, Activity, ActivityLog


@admin.register(Medication, Reminder, Activity, ActivityLog)
class PersonAdmin(admin.ModelAdmin):
    pass
