import json
from django.http import HttpResponse
from django.shortcuts import render
from map.models import Station

# Create your views here.
def index(request):
    context = {
    }
    return render(request, 'map/index.html', context)


def api_station_info(request):
    station_list = Station.objects.all()
    result = []
    for station in station_list:
        result.append({'id': station.id, 'name': station.name, 'latitude': station.latitude, 'longitude': station.longitude})
    
    return HttpResponse(json.dumps(result))
