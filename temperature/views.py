import csv
import io
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.edit import CreateView, DeleteView

from .utilities import import_from_csv, prepare_graph_plot
from .models import TemperatureDisplay


# Create your views here.
class TemperatureDisplayList(ListView):
    model = TemperatureDisplay
    ordering = ['-id']
    template_name = 'dashboard.html'
    context_object_name = 'temps_data'
    paginate_by = 10
    queryset = TemperatureDisplay.objects.all()


class TemperatureDisplayCreate(CreateView):
    model = TemperatureDisplay
    template_name = 'create.html'
    fields = '__all__'


class TemperatureDisplayDelete(DeleteView):
    model = TemperatureDisplay
    template_name = 'delete.html'


def index(request):
    plot_div = prepare_graph_plot(TemperatureDisplay.objects.all())
    return render(request, "index.html", context={'plot_div': plot_div})


def upload_csv(request):
    template = "upload.html"
    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages = {'Error': 'Please provide valid csv file.'}
        return render(request, template, messages)

    __ = import_from_csv(csv_file)

    return redirect(reverse('temperature:dashboard'))
