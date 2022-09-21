import sys
from PyQt5 import QtWidgets as qtw
from DAWidget.DAWidget import DAWidget

class MainWidget(qtw.QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        #self.init_window()
        self.setCentralWidget(DAWidget())
        self.show()

    """ def init_window(self):
        main_layout = qtw.QVBoxLayout(self)

        
        self._init_connect_group()
        self._init_data_group()
        
        main_layout.addWidget(self.connect_groupbox)
        main_layout.addWidget(self.data_groupbox)
        self.setLayout(main_layout)
        
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

    
 """
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWidget()

    sys.exit(app.exec())
