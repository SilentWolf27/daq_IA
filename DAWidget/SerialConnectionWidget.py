from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from arduino.ArduinoSerial import ArduinoSerial
from models.SensorModel import SensorModel


class SerialConnectionWidget(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        connection_layout = qtw.QVBoxLayout()

        # para seleccionar el puerto COM
        self.port_combo = qtw.QComboBox(self)
        self.port_combo.setMinimumSize(100, 25)
        self.port_combo.currentTextChanged.connect(self._change_port)
        connection_layout.addWidget(self.port_combo)
        self.model = qtc.QStringListModel([])
        self.port_combo.setModel(self.model)

        # Boton para conectarse al puerto serie
        self.connect_button = qtw.QPushButton('Conectar', self)
        self.connect_button.setMinimumSize(100, 25)
        self.connect_button.clicked.connect(self.toggle_connect)
        connection_layout.addWidget(self.connect_button)

        # Boton para actualizar la lista de puertos series
        self.update_button = qtw.QPushButton('Actualizar', self)
        self.update_button.setMinimumSize(100, 25)
        self.update_button.clicked.connect(self._refresh_ports)
        connection_layout.addWidget(self.update_button)

        connect_groupbox = qtw.QGroupBox('Conectar Puerto', self)
        connect_groupbox.setMinimumSize(100, 25)
        connect_groupbox.setMaximumWidth(200)
        connect_groupbox.setSizePolicy(
            qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Fixed)
        connect_groupbox.setLayout(connection_layout)

        main = qtw.QVBoxLayout()
        main.addWidget(connect_groupbox)
        self.setLayout(main)

        # Suscripciones
        self._serial = SensorModel()
        self._refresh_ports()
        self._serial_connection_observer = self._serial.subscribe_serial_connection(
            self.on_serial_connect)

    def _refresh_ports(self):
        ports = ArduinoSerial.port_list()
        self.model.setStringList(ports)

        if (len(ports) > 0):
            self.port_combo.setCurrentIndex(0)
            self._serial.port = ports[0]

    def _change_port(self, name: str):
        self._serial.port = name

    def on_serial_connect(self, is_open):
        if is_open:
            self._connect()
        else:
            self._disconnect()

    def toggle_connect(self):
        self._serial.toggle_serial_open()

    def _connect(self):
        self.connect_button.setText('Desconectar')
        self.port_combo.setEnabled(False)
        self.update_button.setEnabled(False)

    def _disconnect(self):
        self.connect_button.setText('Conectar')
        self.port_combo.setEnabled(True)
        self.port_combo.setCurrentIndex(-1)
        self.update_button.setEnabled(True)

    @property
    def serial(self) -> ArduinoSerial:
        return self._serial
