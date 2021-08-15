from django.db import models


# Create your models here.

class TemperatureDisplay(models.Model):
    x_axis = models.DecimalField(max_digits=30, decimal_places=15)
    y_axis = models.DecimalField(max_digits=30, decimal_places=15)
    temperature = models.DecimalField(max_digits=30, decimal_places=15)
