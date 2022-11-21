import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from DAWidget.DAWidget import DAWidget
from models.DAQModel import DAQModel
from qt_material import apply_stylesheet
from models.SensorModel import SensorModel
from arduino.ArduinoSerial import ArduinoSerial
from DAWidget.StatusWidget import StatusWidget


class MainWidget(qtw.QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        serial = ArduinoSerial()
        self.sensor_model = SensorModel('G', serial)

        self.setCentralWidget(DAWidget())
        self.setWindowTitle('Herramienta DAQ')

        save_icon = self.style().standardIcon(qtw.QStyle.SP_DialogSaveButton)
        toolbar = self.addToolBar('Archivo')
        toolbar.addAction(save_icon, 'Guardar', self.saveFile)
        toolbar.setMovable(False)
        toolbar.setFloatable(False)

        statusbar = qtw.QStatusBar()
        status_widget = StatusWidget()
        status_widget.setSizePolicy(
            qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        statusbar.addWidget(status_widget)
        statusbar.setSizeGripEnabled(False)
        self.setStatusBar(statusbar)

        self.setMinimumSize(1000, 500)
        self.show()

    def saveFile(self):
        model = DAQModel()
        if not model.saving:
            filename, _ = qtw.QFileDialog.getSaveFileName(
                self, caption="Guardar archivo:",
                directory=qtc.QDir.homePath(),
                filter='CSV Files (*.csv)')
            if filename:
                extension = '' if filename.endswith('.csv') else '.csv'
                model.save(filename + extension)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_blue.xml')
    mw = MainWidget()

    sys.exit(app.exec())
