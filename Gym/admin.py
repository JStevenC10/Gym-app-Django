from django.contrib import admin

from .models import ClientGym, Trainers
# Register your models here.
admin.site.register([ClientGym, Trainers]) 