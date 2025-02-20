from rest_framework.exceptions import ValidationError

from rest_framework import serializers
from .models import *

class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['full_name', 'contact_info', 'office']

class DoctorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['office', 'contact_info']


class PatientListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Patient
        fields = ['last_name', 'age', 'gender', 'id']

class PatientRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'price']

class ServiceRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class VisitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

class VisitRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitCreateOrUpdateSerializer(serializers.ModelSerializer):

    def get_validator_schedule(self,value):
        visit_count = value.objects.count()
        if 24 <= visit_count:
            raise ValidationError('Schedule is full')
        return value

    class Meta:
        model = Visit
        fields = '__all__'


class ScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class ScheduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class ScheduleCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'



















