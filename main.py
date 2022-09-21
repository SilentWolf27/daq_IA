import sys
from PyQt5 import QtWidgets as qtw
from chart.chartWidget import SensorChart

class MainWidget(qtw.QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        #self._serial = ArduinoSerial(baudrate=9600, timeout=0.5)
        #self.init_window()
        self.setCentralWidget(SensorChart())
        self.show()

    """ def init_window(self):
        main_layout = qtw.QVBoxLayout(self)

        
        self._init_connect_group()
        self._init_data_group()
        
        main_layout.addWidget(self.connect_groupbox)
        main_layout.addWidget(self.data_groupbox)
        self.setLayout(main_layout)
        
    def _init_connect_group(self):
        self.connection_layout = qtw.QVBoxLayout()

        #para seleccionar el puerto COM
        self.port_combo = qtw.QComboBox(self)
        self.port_combo.setMinimumSize(100, 25)
        self.port_combo.currentTextChanged.connect(self._change_port)
        self.connection_layout.addWidget(self.port_combo)
        self._refresh_ports()

        #Boton para conectarse al puerto serie
        self.connect_button = qtw.QPushButton('Conectar', self)
        self.connect_button.setMinimumSize(100, 25)
        self.connect_button.clicked.connect(self._connect)
        self.connection_layout.addWidget(self.connect_button)

         #Boton paraactualizar la lista de puertos series
        self.update_button = qtw.QPushButton('Actualizar', self)
        self.update_button.setMinimumSize(100, 25)
        self.update_button.clicked.connect(self._refresh_ports)
        self.connection_layout.addWidget(self.update_button)

        self.connect_groupbox = qtw.QGroupBox('Conectar Puerto', self) 
        self.connect_groupbox.setMinimumSize(100, 25)
        self.connect_groupbox.setMaximumWidth(200)
        self.connect_groupbox.setSizePolicy(qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Fixed)
        self.connect_groupbox.setLayout(self.connection_layout)

    def _init_data_group(self):
        self.data_layout = qtw.QVBoxLayout()

        #Para ingresar el nombre del archivo generado
        self.file_name = qtw.QLineEdit(
            '', self, placeholderText='Nombre del archivo', maxLength=20)
        self.file_name.setMinimumSize(100, 25)
        self.file_name.setMaximumWidth(500)
        self.file_name.setSizePolicy(qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Fixed)
        self.data_layout.addWidget(self.file_name)

        #Boton para iniciar o pausar la adquisicion de datos

        #Boton para detener y guardar la adquisicion de datos
       
        self.data_groupbox = qtw.QGroupBox('Adquisición de datos', self) 
        self.data_groupbox.setMinimumSize(100, 25)
        self.data_groupbox.setMaximumWidth(200)
        self.data_groupbox.setSizePolicy(qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Fixed)
        self.data_groupbox.setLayout(self.data_layout)

    def _refresh_ports(self):
        ports = ArduinoSerial.port_list()
        self.port_combo.addItems(ports)

        if(len(ports) > 0):
            self.port_combo.setCurrentIndex(0)
            self._serial.port = ports[0]

    def _connect(self):
        if not self._serial.port is None:
            try: 
                if self._serial.test_connection():
                    self.connect_button.setText('Desconectar')
                    self.connect_button.clicked.connect(self._disconnect)
                    self.port_combo.setEnabled(False)
            except:
                print(sys.exc_info()[0])
        
    def _disconnect(self):
        pass
    
    def _change_port(self, name: str):
        self._serial.port = name
 """
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWidget()

    sys.exit(app.exec())
