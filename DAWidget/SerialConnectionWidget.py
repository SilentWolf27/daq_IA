from PyQt5 import  QtWidgets as qtw
from PyQt5 import QtCore as qtc
from arduino.ArduinoSerial import ArduinoSerial
import sys

class SerialConnectionWidget(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self._serial = ArduinoSerial(baudrate=9600, timeout=0.5)
        self.connected: bool = False

        connection_layout = qtw.QVBoxLayout()

        #para seleccionar el puerto COM
        self.port_combo = qtw.QComboBox(self)
        self.port_combo.setMinimumSize(100, 25)
        self.port_combo.currentTextChanged.connect(self._change_port)
        connection_layout.addWidget(self.port_combo)
        self.model = qtc.QStringListModel([])
        self.port_combo.setModel(self.model)
        self._refresh_ports()

        #Boton para conectarse al puerto serie
        self.connect_button = qtw.QPushButton('Conectar', self)
        self.connect_button.setMinimumSize(100, 25)
        self.connect_button.clicked.connect(self.serial_event())
        connection_layout.addWidget(self.connect_button)

        #Boton para actualizar la lista de puertos series
        self.update_button = qtw.QPushButton('Actualizar', self)
        self.update_button.setMinimumSize(100, 25)
        self.update_button.clicked.connect(self._refresh_ports)
        connection_layout.addWidget(self.update_button)

        connect_groupbox = qtw.QGroupBox('Conectar Puerto', self) 
        connect_groupbox.setMinimumSize(100, 25)
        connect_groupbox.setMaximumWidth(200)
        connect_groupbox.setSizePolicy(qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Fixed)
        connect_groupbox.setLayout(connection_layout)

        main = qtw.QVBoxLayout()
        main.addWidget(connect_groupbox)
        self.setLayout(main)

    def _refresh_ports(self):
        ports = ArduinoSerial.port_list()
        self.model.setStringList(ports)

        if(len(ports) > 0):
            self.port_combo.setCurrentIndex(0)
            self._serial.port = ports[0]

    def _change_port(self, name: str):
        self._serial.port = name

    def setSerialEvent(self, on_connect, on_disconnect):
        try:
            self.connect_button.clicked.disconnect()
            self.connect_button.clicked.connect(self.serial_event(on_connect, on_disconnect))
        except: pass

    def serial_event(self, on_connect = None, on_disconnect = None):
        def handle_serial():
            if self.connected:
                self._disconnect(on_disconnect)
            else:
                self._connect(on_connect)
    
        return handle_serial

    def _connect(self, callback = None):
        if not self._serial.port is None:
            try: 
                if self._serial.test_connection():
                    self.connected = True
                    self.connect_button.setText('Desconectar')
                    self.port_combo.setEnabled(False)
                    
                    if callback:
                        callback()
            except:
                print(sys.exc_info()[0])
        
    def _disconnect(self, callback=None):
        if callback:
            callback()

    @property
    def serial(self) -> ArduinoSerial:
        return self._serial