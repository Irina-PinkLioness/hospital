# Generated by Django 5.1.5 on 2025-02-09 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0005_alter_visit_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='doctor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedules', to='med.doctor'),
        ),
    ]
