from django.urls import path
from .views import (
    medication_list, reminder_list, create_medication, create_reminder,
    delete_medication, delete_reminder, activity_list, log_activity,
    delete_activity_log
)

urlpatterns = [
    path('medications/', medication_list, name='medication_list'),
    path('reminders/', reminder_list, name='reminder_list'),
    path('medications/create/', create_medication, name='create_medication'),
    path('reminders/create/', create_reminder, name='create_reminder'),
    path('medications/delete/<int:pk>/', delete_medication, name='delete_medication'),
    path('reminders/delete/<int:pk>/', delete_reminder, name='delete_reminder'),
    path('activities/', activity_list, name='activity_list'),
    path('activities/log/', log_activity, name='log_activity'),
    path('activities/delete/<int:pk>/', delete_activity_log, name='delete_activity_log'),
]