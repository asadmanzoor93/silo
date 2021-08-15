from django.contrib import admin

# Register your models here.
from .models import TemperatureDisplay


class TemperatureDisplayAdmin(admin.ModelAdmin):
    list_display = ('x_axis', 'y_axis', 'temperature')


admin.site.register(TemperatureDisplay, TemperatureDisplayAdmin)
