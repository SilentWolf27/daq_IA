from typing import List
from PyQt5 import QtWidgets as qtw
from DAWidget.chartWidget import SensorChart
from models.SensorModel import SensorModel

class SensorChartTabs(qtw.QWidget):
    def __init__(self, sensors: List[str]) -> None:
        super().__init__()

        self.tabs = qtw.QTabWidget()
        self.charts = [SensorChart(sensor) for sensor in sensors]

        for chart in self.charts:
            self.tabs.addTab(chart, chart.title)

        main_layout = qtw.QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

        sensor_model = SensorModel()
        self.data_observer = sensor_model.subscribe_values(self.printData)

    def add_data(self, data: List[float]):
        if not data is None:
            for idx, value in enumerate(data):
                self.charts[idx].add_data(value)

    def printData(self, values):
        print(values)
