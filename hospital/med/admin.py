from django.contrib import admin
from .models import *

admin.site.register(Office)
admin.site.register(Patient)
admin.site.register(Service)
admin.site.register(Doctor)
admin.site.register(Visit)
admin.site.register(Schedule)
admin.site.register(Notification)
