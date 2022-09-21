from ast import main
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from DAWidget.SerialConnectionWidget import SerialConnectionWidget
from DAWidget.chartWidget import SensorChart
from arduino.ArduinoSensor import ArduinoSensor

class DAWidget(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()

        main_layout = qtw.QHBoxLayout()
        left_layout = qtw.QVBoxLayout() #Layour barra lateral

        #elementos barra lateral 
        serial_connect = SerialConnectionWidget()
        serial_connect.setSerialEvent(self.start_timer, self.stop_timer)

        left_layout.addWidget(serial_connect)
        #Sensores que se adquiriran los datos
        self.sensor = ArduinoSensor('G', serial_connect.serial)


        #Graficas
        self.charts = SensorChart('Gyro')

        main_layout.addItem(left_layout)
        main_layout.addWidget(self.charts)
        self.setLayout(main_layout)

        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.timer_event)

    def start_timer(self):
        self.timer.setInterval(1000)
        self.timer.start()

    def stop_timer(self):
        self.timer.stop()

    def timer_event(self):
        print(self.sensor.value)