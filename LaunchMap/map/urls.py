from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api_station_info', views.api_station_info, name='api_station_info'),
    path('api_weather', views.api_weather, name='api_weather'),
    path('api_can_launch', views.api_can_launch, name='api_can_launch'),
    path('api_cannot_launch', views.api_cannot_launch, name='api_cannot_launch'),
]