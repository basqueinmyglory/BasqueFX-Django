from django.shortcuts import render
from .models import Dailyforecast

# Create your views here.
def home(request):
    dailyforecast = Dailyforecast.objects.order_by('-entry_date')
    return render(request, 'forecasts/home.html', {'dailyforecast': dailyforecast} )

def tools(request):
    return render(request, 'forecasts/tools.html')