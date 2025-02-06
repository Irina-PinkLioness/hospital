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

class Visit(models.Model):
    STATUS_CHOICES = {
        "PL": "planned",
        "CO": "completed",
        "CA": "cancelled"
    }
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    visit_time = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name= 'visits')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name= 'visits')
    service =models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.doctor.full_name} - {self.patient.full_name} - {self.visit_time}"






