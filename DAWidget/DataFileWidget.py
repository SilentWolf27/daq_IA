from PyQt5 import QtWidgets as qtw

from models.DAQModel import DAQModel
from models.SensorModel import SensorModel


class DataFileWidget(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.daq = DAQModel()

        data_layout = qtw.QVBoxLayout()

        # Para el nombre de la etiqueta de salida
        self.label_input = qtw.QLineEdit()
        self.label_input.setPlaceholderText('Etiqueta de salida')
        self.label_input.setMinimumSize(100, 25)
        data_layout.addWidget(self.label_input)

        # Boton iniciar o detener la adquisicion
        self.start_button = qtw.QPushButton('Iniciar', self)
        self.start_button.setMinimumSize(100, 25)
        self.start_button.setEnabled(False)
        self.start_button.clicked.connect(self.data_event())
        data_layout.addWidget(self.start_button)

        # Boton borrar los datos
        self.clear_button = qtw.QPushButton('Borrar datos', self)
        self.clear_button.setMinimumSize(100, 25)
        self.clear_button.setEnabled(False)
        self.clear_button.clicked.connect(self.clear_data)
        data_layout.addWidget(self.clear_button)

        data_groupbox = qtw.QGroupBox('Adquisición de datos', self)
        data_groupbox.setMinimumSize(100, 25)
        data_groupbox.setMaximumWidth(200)
        data_groupbox.setSizePolicy(
            qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Fixed)
        data_groupbox.setLayout(data_layout)

        main = qtw.QVBoxLayout()
        main.addWidget(data_groupbox)
        self.setLayout(main)

        sensor_model = SensorModel()
        self.data_observer = sensor_model.subscribe_values(self.printData)

    def setDataEvent(self, data_start, data_stop):
        try:
            self.connect_button.clicked.disconnect()
            self.connect_button.clicked.connect(
                self.data_event(data_start, data_stop))
        except:
            pass

    def data_event(self, data_start=None, data_stop=None):
        def handle_data():
            if self.daq.saving:
                self._stop(data_stop)
            else:
                self._start(data_start)

        return handle_data

    def _start(self, callback=None):
        if self.label_input.text() != '':
            self.daq.saving = True
            self.start_button.setText('Detener')
            self.clear_button.setEnabled(False)
            self.label_input.setStyleSheet("border: 1px solid black")

            if callback:
                callback()
        else:
            self.label_input.setStyleSheet("border: 2px solid red")

    def _stop(self, callback=None):
        self.daq.saving = False
        self.start_button.setText('Iniciar')
        self.clear_button.setEnabled(True)
        if callback:
            callback()

    def add_data(self, data):
        if self.daq.saving:
            self.daq.append(data, self.label_input.text())

    def clear_data(self):
        self.daq.clear()

    def enable(self):
        self.start_button.setEnabled(True)


    def printData(self, values):
        print(values)