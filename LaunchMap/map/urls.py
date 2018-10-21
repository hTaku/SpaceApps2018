from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api_station_info', views.api_station_info, name='api_station_info'),
]