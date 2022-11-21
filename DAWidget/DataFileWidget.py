from PyQt5 import QtWidgets as qtw

from models.DAQModel import DAQModel
from models.SensorModel import SensorModel
from models.StatusModel import StatusModel
from models.SensorModel import SensorModel

class DataFileWidget(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.daq_model = DAQModel()
        self._data_observer = None

        data_layout = qtw.QVBoxLayout()

        # Para el nombre de la etiqueta de salida
        self.label_input = qtw.QLineEdit()
        self.label_input.setPlaceholderText('Etiqueta de salida')
        self.label_input.setMinimumSize(150, 25)
        data_layout.addWidget(self.label_input)

        # Boton iniciar o detener la adquisicion
        self.start_button = qtw.QPushButton('Iniciar', self)
        self.start_button.setMinimumSize(150, 25)
        self.start_button.setEnabled(False)
        self.start_button.clicked.connect(self.data_event)
        data_layout.addWidget(self.start_button)

        # Boton borrar los datos
        self.clear_button = qtw.QPushButton('Borrar', self)
        self.clear_button.setMinimumSize(150, 25)
        self.clear_button.setEnabled(False)
        self.clear_button.clicked.connect(self.clear_data)
        data_layout.addWidget(self.clear_button)

        data_groupbox = qtw.QGroupBox('Adquisición de datos', self)
        data_groupbox.setMinimumSize(150, 25)
        data_groupbox.setMaximumWidth(200)
        data_groupbox.setSizePolicy(
            qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Fixed)
        data_groupbox.setLayout(data_layout)

        main = qtw.QVBoxLayout()
        main.addWidget(data_groupbox)
        self.setLayout(main)

        # Observers
        self.sensor_model = SensorModel()
        self._serial_connection_observer = self.sensor_model.subscribe_serial_connection(
            self.on_serial_connect)

        self._save_data_observer = self.daq_model.subscribe_data_saving(
            self.on_data_saving_change)

        self.status_model = StatusModel()


    def data_event(self):
        self.daq_model.toggle_save()

    def on_serial_connect(self, value):
        if value:
            self.enable()
        else:
            self._stop()
            self.disable()

    def on_data_saving_change(self, is_saving):
        if is_saving:
            self._start()
        else:
            self._stop()

    def _start(self):
        if self.label_input.text() != '':
            self.start_button.setText('Detener')
            self.clear_button.setEnabled(False)
            self.label_input.setStyleSheet("border: 1px solid black")

            self._data_observer = self.sensor_model.subscribe_values(
                self.add_data)
            self.status_model.data_status = 'Adquisición de datos en curso'
        else:
            self.label_input.setStyleSheet("border: 2px solid red")

    def _stop(self):
        self.start_button.setText('Iniciar')
        self.clear_button.setEnabled(True)
        if not self._data_observer is None:
            self._data_observer.dispose()
            self.status_model.data_status = f"Adquisición de datos detenida: {self.daq_model.length} datos guardados"

    def add_data(self, data):
        self.daq_model.append(data, self.label_input.text())

    def clear_data(self):
        self.label_input.setText('')
        self.daq_model.clear()
        if not self._data_observer is None:
            self.status_model.data_status = f"Adquisición de datos detenida: {self.daq_model.length} datos guardados"

    def enable(self):
        self.start_button.setEnabled(True)

    def disable(self):
        self.start_button.setEnabled(False)
