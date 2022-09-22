from PyQt5 import QtChart as qtch
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class SensorChart(qtch.QChartView):
    MAX_LEN = 100

    def __init__(self, title='Titulo') -> None:
        super().__init__()
        self.count = 0

        # create chart
        chart = qtch.QChart()
        chart.setTitle(title)
        chart.legend().setVisible(False)
        self.setChart(chart)

        # series
        self.series = qtch.QLineSeries()
        chart.addSeries(self.series)

        # Axes
        x_axis = qtch.QValueAxis()
        x_axis.setRange(0, self.MAX_LEN)
        y_axis = qtch.QValueAxis()
        y_axis.setRange(0, self.MAX_LEN)
        chart.setAxisX(x_axis, self.series)
        chart.setAxisY(y_axis, self.series)

    def add_data(self, data: float | int):
        self.series.append(self.count, data)
        self.update_y_axis(data)
        
        if self.count >= self.MAX_LEN - 1:
            self.update_x_axis()

        self.count += 1

    def update_x_axis(self):
        x_axis = self.chart().axisX()
        min = x_axis.min()
        max = x_axis.max()

        x_axis.setMax(max + 1)
        x_axis.setMin(min + 1)

    def update_y_axis(self, value: float | int):
        y_axis = self.chart().axisY()
        min = y_axis.min()
        max = y_axis.max()

        if value > max:
            y_axis.setMax(value + 10)

        elif value < min:
            y_axis.setMin(value - 10)

    @property
    def title(self):
        return self.chart().title()