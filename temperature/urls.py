"""
URL Configuration
"""
from django.urls import path, reverse

from .views import (
    TemperatureDisplayList,
    TemperatureDisplayDelete,
    TemperatureDisplayCreate,
    index,
    upload_csv
)
from .models import TemperatureDisplay

app_name = 'temperature'

urlpatterns = [
    path('', index, name='index'),
    path('upload_csv', upload_csv, name='upload_csv'),
    path('dashboard', TemperatureDisplayList.as_view(), name='dashboard'),
    path('create', TemperatureDisplayCreate.as_view(success_url="/dashboard"), name='create'),
    path('delete/<int:pk>', TemperatureDisplayDelete.as_view(success_url="/dashboard"), name='delete'),
]
