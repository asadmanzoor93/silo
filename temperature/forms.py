from django import forms
from .models import TemperatureDisplay


class TemperatureDisplayForm(forms.ModelForm):
    class Meta:
        model = TemperatureDisplay
