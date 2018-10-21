from django.contrib import admin
from .models import Country, Station, WeatherMaster

# Register your models here.
admin.site.register(Country)
admin.site.register(Station)
admin.site.register(WeatherMaster)
