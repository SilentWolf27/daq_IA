from typing import List
from PyQt5 import QtWidgets as qtw
from DAWidget.chartWidget import SensorChart
from models.SensorModel import SensorModel


class SensorChartTabs(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.tabs = qtw.QTabWidget()
        self.charts = []

        main_layout = qtw.QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

        sensor_model = SensorModel()
        self.data_observer = sensor_model.subscribe_values(self.add_data)
        self.labels_observer = sensor_model.labels.subscribe(
            self.handle_labels)

    def add_data(self, data: List[float]):
        try:
            if not data is None:
                for idx, value in enumerate(data):
                    self.charts[idx].add_data(value)
        except:
            pass

    def handle_labels(self, labels):
        self.tabs.clear()
        self.charts = [SensorChart(label) for label in labels]

        for chart in self.charts:
            self.tabs.addTab(chart, chart.title)
