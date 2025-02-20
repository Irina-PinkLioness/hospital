import datetime
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete
from pyexpat.errors import messages
from .models import Visit, Notification, Patient, Doctor


@receiver(post_save, sender=Visit)
def notify_about_new_visit(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            sender=instance.patient.user,
            recipient=instance.schedule.doctor.user,
            message=f'New visit is on {instance.schedule.timestamp_start}.',
            notification_type=Notification.NEW_VISIT
        )

@receiver(pre_save, sender=Visit)
def notify_about_cancelled_visit(sender, instance, **kwargs):
    if instance.status == Visit.CANCELLED:
        Notification.objects.create(
            sender=instance.patient.user,
            recipient=instance.schedule.doctor.user,
            message="VISIT is CANCELED",
            notification_type=Notification.VISIT_CANCELED
        )


@receiver(pre_delete, sender=Patient)
def delete_related_visits(sender, instance, **kwargs):
    related_visits = Visit.objects.filter(patient=instance)
    for visit in related_visits:
        Notification.objects.create(
            sender=instance.user,
            recipient=visit.schedule.doctor.user,
            message="VISIT is CANCELED",
            notification_type=Notification.VISIT_CANCELED
        )




