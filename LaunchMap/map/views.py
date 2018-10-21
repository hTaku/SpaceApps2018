import json
from django.http import HttpResponse
from django.shortcuts import render
from map.models import Station, Weather, WeatherMaster

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

def api_weather(request):
    id = request.GET.get('id')

    weather = Weather.objects.select_related('station').filter(station_id=id).all()[0]

    result = {'weather': 'sun', 'wind': {'speed': weather.wind_speed, 'deg': weather.wind_degree}}
    
    return HttpResponse(json.dumps(result))

def api_can_launch(request):
    return HttpResponse(json.dumps({'result': 'OK'}))

def api_cannot_launch(request):
    return HttpResponse(json.dumps({'result': 'OK'}))
