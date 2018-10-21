from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=2)
    name_full = models.CharField(max_length=60)
    name_jp = models.CharField(max_length=60)

class Station(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_id = models.IntegerField(default=0)
    name = models.CharField(max_length=120)
    name_alias = models.CharField(max_length=60, default='')
    name_jp = models.CharField(max_length=120)
    latitude = models.FloatField()
    longitude = models.FloatField()
    time_zone = models.CharField(max_length=24, default='')

class LaunchSchedule(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    image = models.CharField(max_length=1024)
    date = models.DateField()
    window_start = models.TimeField()
    window_end = models.TimeField()
    summary = models.CharField(max_length=1024)
    detail = models.CharField(max_length=10000)
    movie = models.CharField(max_length=1024)
    update = models.DateTimeField(auto_now=True)

class WeatherMaster(models.Model):
    weather_name = models.CharField(max_length=12)

class Weather(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    days = models.IntegerField(default=16)
    dt = models.IntegerField(default=0)
    weathermaster = models.ForeignKey(WeatherMaster, on_delete=models.CASCADE)
    wind_speed = models.IntegerField(default=0)
    wind_degree = models.FloatField(default=0.0)
    cloud = models.IntegerField(default=0)


