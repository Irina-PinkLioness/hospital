# Generated by Django 5.1.5 on 2025-02-02 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='visit',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='med.doctor'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='med.patient'),
        ),
    ]
