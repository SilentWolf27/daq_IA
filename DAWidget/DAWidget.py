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
        self.serial_connect.setSerialEvent(
            on_connect=self.start_timer, on_disconnect=self.stop_timer)

        self.data_connect = DataFileWidget()
        left_layout.addWidget(self.serial_connect)
        left_layout.addWidget(self.data_connect)
        # Sensores que se adquiriran los datos
        self.sensor = ArduinoSensor('G', self.serial_connect.serial)

        # Graficas
        sensor_model = SensorModel()
        self.tab = SensorChartTabs(sensor_model.sensors)

        main_layout.addItem(left_layout)
        main_layout.addWidget(self.tab)
        self.setLayout(main_layout)

        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.timer_event)

    def start_timer(self):
        self.timer.setInterval(250)
        self.timer.start()

    def stop_timer(self):
        self.timer.stop()

    def timer_event(self):
        data = self.sensor.value
        self.tab.add_data(data)
