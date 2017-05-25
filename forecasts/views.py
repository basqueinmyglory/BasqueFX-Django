from django.shortcuts import render
from .models import Dailyforecast, Calevents

# Create your views here.
def home(request):
    return render(request, 'forecasts/home.html')

def tools(request):
    dailyforecast = Dailyforecast.objects.order_by('-entry_date')[0]
    dailyevents = Calevents.objects.order_by('-date')
    return render(request, 'forecasts/tools.html', {'dailyevents': dailyevents, 'dailyforecast':dailyforecast})