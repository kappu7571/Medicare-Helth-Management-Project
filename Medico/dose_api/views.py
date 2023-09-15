from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Medication, Reminder, Activity, ActivityLog
from .serializers import MedicationSerializer, ReminderSerializer, ActivitySerializer, ActivityLogSerializer


@api_view(['GET'])
def medication_list(request):
    medications = Medication.objects.all()
    serializer = MedicationSerializer(medications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def reminder_list(request):
    reminders = Reminder.objects.all()
    serializer = ReminderSerializer(reminders, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_medication(request):
    serializer = MedicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_reminder(request):
    serializer = ReminderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_medication(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    medication.delete()
    return Response(status=204)


@api_view(['DELETE'])
def delete_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    reminder.delete()
    return Response(status=204)


@api_view(['GET'])
def activity_list(request):
    activities = Activity.objects.all()
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def log_activity(request):
    serializer = ActivityLogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_activity_log(request, pk):
    activity_log = get_object_or_404(ActivityLog, pk=pk)
    activity_log.delete()
    return Response(status=204)
