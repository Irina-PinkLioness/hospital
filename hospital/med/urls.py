from django.urls import path
from .views import DoctorView, PatientView, ServiceView, VisitView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('doctor/', DoctorView.as_view({
        'get': 'list',
        'post': 'create'
        })
    ),
    path('doctor/<int:id>/', DoctorView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
        })
    ),
    path('doctor/<int:id>/patient/', DoctorView.as_view({
        'get': 'list_patient'
        })
    ),
    path('patient/', PatientView.as_view({
        'get': 'list',
        'post': 'create'
    })
         ),
    path('patient/<int:id>/', PatientView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })
         ),
    path('service/', ServiceView.as_view({
        'get': 'list',
        'post': 'create'
    })
         ),
    path('visit/', VisitView.as_view({
        'get': 'list',
        'post': 'create'
    })
         ),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
