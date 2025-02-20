import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .permissions import RoleBasedPermissionsMixin, HasPermissionByAuthUserRole
from .serializers import (DoctorListSerializer, DoctorRetrieveSerializer, DoctorCreateSerializer,
                          DoctorUpdateSerializer, PatientListSerializer, ServiceListSerializer,
                          ServiceRetrieveSerializer, VisitListSerializer, VisitRetrieveSerializer,
                          PatientRetrieveSerializer, PatientCreateOrUpdateSerializer,ServiceCreateOrUpdateSerializer,
                          VisitCreateOrUpdateSerializer, ScheduleListSerializer,ScheduleRetrieveSerializer,
                          ScheduleCreateOrUpdateSerializer)


class DoctorView(
    RoleBasedPermissionsMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['last_name', 'office']
    search_fields = ['first_name', 'last_name', 'office']
    permission_classes = [IsAuthenticated, HasPermissionByAuthUserRole]

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        if self.action == 'retrieve':
            return DoctorRetrieveSerializer
        if self.action == 'create':
            return DoctorCreateSerializer
        if self.action == 'update':
            return DoctorUpdateSerializer
        if self.action == 'list_patient':
            return PatientListSerializer

    def get_queryset(self):
        if self.action == 'list_patient':
            return Patient.objects.all()
        return Doctor.objects.all()

    def list_patient(self,request, id):
        queryset = self.get_queryset().filter(visits__id=id).all()
        serializer = self.get_serializer(queryset , many=True)
        return Response(data=serializer.data)

    def get_action_permissions(self):
        if self.action in('list', 'retrieve'):
            self.action_permissions = ['view_doctor', ]
        elif self.action == 'list_patient':
            self.action_permissions = ['view_patient', ]
        else:
            self.action_permissions = []


class PatientView(
    RoleBasedPermissionsMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['gender']
    search_fields = ['first_name', 'last_name', 'age']
    permission_classes = [IsAuthenticated, HasPermissionByAuthUserRole]

    def get_queryset(self):
        return Patient.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer
        if self.action == 'retrieve':
            return PatientRetrieveSerializer
        if self.action == 'create':
            return PatientCreateOrUpdateSerializer
        if self.action == 'update':
            return PatientCreateOrUpdateSerializer

    def get_action_permissions(self):
        if self.action in('list', 'retrieve'):
            self.action_permissions = ['view_patient', ]
        elif self.action == 'create':
            self.action_permissions = ['add_patient', ]
        else:
            self.action_permissions = []


class VisitView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return VisitListSerializer
        if self.action == 'retrieve':
            return VisitRetrieveSerializer
        if self.action == 'create':
            return VisitCreateOrUpdateSerializer
        if self.action == 'update':
            return VisitCreateOrUpdateSerializer

    def get_queryset(self):
        if self.action == 'get_analytics':
            Visit.objects.filter(
                schedule__timestamp_start__lt=datetime.date.today()
            ).count()
        return Visit.objects.all()

    def get_analytics(self, request):
        response = {
            'visit_count': Visit.objects.filter(
                schedule__timestamp_start__lt=datetime.date.today()
            ).count()
        }
        return Response(status=status.HTTP_200_OK, data=response)

class ServiceView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
   def get_serializer_class(self):
        if self.action == 'list':
            return ServiceListSerializer
        if self.action == 'retrieve':
            return ServiceRetrieveSerializer
        if self.action == 'create':
            return ServiceCreateOrUpdateSerializer
        if self.action == 'update':
            return ServiceCreateOrUpdateSerializer

   def get_queryset(self):
       return Service.objects.all()


class ScheduleView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return ScheduleListSerializer
        if self.action == 'retrieve':
            return ScheduleRetrieveSerializer
        if self.action == 'create':
            return ScheduleCreateOrUpdateSerializer
        if self.action == 'update':
            return ScheduleCreateOrUpdateSerializer

    def get_queryset(self):
        return Schedule.objects.all()





