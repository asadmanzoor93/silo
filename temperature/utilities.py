import io
import csv
from plotly.offline import plot
from plotly.graph_objs import Scatter

from .models import TemperatureDisplay


def import_from_csv(csv_file):
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    try:
        line = csv.reader(io_string, delimiter=',')
        for item in line:
            temp_data = dict(
                x_axis=item[0],
                y_axis=item[1],
                temperature=item[2]
            )

            TemperatureDisplay.objects.create(**temp_data)
    except Exception as e:
        pass


def prepare_graph_plot(temps_data):
    x_data = [temp_data.x_axis for temp_data in temps_data]
    y_data = [temp_data.y_axis for temp_data in temps_data]

    return plot([Scatter(
        x=x_data,
        y=y_data,
        mode='lines',
        name='temperatures',
        opacity=0.8,
        marker_color='green'
    )],
        output_type='div'
    )
