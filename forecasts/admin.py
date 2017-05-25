from django.contrib import admin
from .models import Dailyforecast, Calevents

# Register your models here.
admin.site.register(Dailyforecast)
admin.site.register(Calevents)