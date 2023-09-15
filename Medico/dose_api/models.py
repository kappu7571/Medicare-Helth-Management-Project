from django.db import models


class Medication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Reminder(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    reminder_date = models.DateField()
    reminder_time = models.TimeField()

    def __str__(self):
        return f"{self.medication} - {self.reminder_date} {self.reminder_time}"


class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class ActivityLog(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return f"{self.activity} - {self.date}"
