import timestamp
from django.contrib.auth.models import User
from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=100)
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Patient(models.Model):
    STATUS_CHOICES = {
        "M": "male",
        "F": "female"
    }
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DateField()
    gender = models.CharField(max_length=1, choices=STATUS_CHOICES)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    timestamp_start = models.DateTimeField()
    timestamp_end = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL, related_name='schedules')

    def __str__(self):
        return '%s %s' % (self.doctor.full_name, str(self.timestamp_start))


def get_start(schedule='schedule'):
    if schedule:
        return Schedule.timestamp_start
    else:
        return "Visits closed"


class Visit(models.Model):
    PLANNED = "planned"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    STATUS_CHOICES = {
        "PL": "planned",
        "CO": "completed",
        "CA": "cancelled"
    }
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name= 'visits')
    service =models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    schedule = models.OneToOneField(Schedule, null=True, on_delete=models.CASCADE, related_name= 'visits')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.schedule}"


class Notification(models.Model):
    STATUS_CHOICES = {
        "NEW": "new",
        "READ": "reading",
        "ARCH": "archived"
    }
    NEW_VISIT = "NEW_VISIT"
    VISIT_CANCELED = "VISIT_CANCELED"
    OTHER = "OTHER"
    TYPE_CHOICES = {
        "NEW_VISIT": "new visit",
        "CANCEL": "visit cancelled",
        "OTHER": "other"
    }

    sender = models.ForeignKey(User, related_name='send_notification', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_notification', on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="NEW")
    notification_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=OTHER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sender} -> {self.recipient} : {self.message[:300]}'

    class Mets:
        ordering = ['-created_at']

        



















