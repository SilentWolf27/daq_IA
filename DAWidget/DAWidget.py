from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from DAWidget.DataFileWidget import DataFileWidget
from DAWidget.SerialConnectionWidget import SerialConnectionWidget
from arduino.ArduinoSensor import ArduinoSensor
from DAWidget.ChartTabs import SensorChartTabs
from models.SensorModel import SensorModel


class DAWidget(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()

        main_layout = qtw.QHBoxLayout()
        left_layout = qtw.QVBoxLayout()  # Layour barra lateral

        # elementos barra lateral
        self.serial_connect = SerialConnectionWidget()

        self.data_connect = DataFileWidget()
        left_layout.addWidget(self.serial_connect)
        left_layout.addWidget(self.data_connect)

        # Graficas
        sensor_model = SensorModel()
        self.tab = SensorChartTabs(sensor_model.labels)

        # Sensores que se adquiriran los datos
        self.sensor = ArduinoSensor(sensor_model.command, self.serial_connect.serial)

        main_layout.addItem(left_layout)
        main_layout.addWidget(self.tab)
        self.setLayout(main_layout)

        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.timer_event)
        self.sensor_model = SensorModel()
        self._serial_connection_observer = self.sensor_model.subscribe_serial_connection(
            self.on_serial_connect)

    def start_timer(self):
        self.timer.setInterval(250)
        self.timer.start()

    def stop_timer(self):
        self.timer.stop()

    def timer_event(self):
        self.sensor_model.read_value()

    def on_serial_connect(self, is_open):
        if is_open:
            self.start_timer()
        else:
            self.stop_timer()