import sys
from PyQt5 import QtWidgets as qtw
from DAWidget.DAWidget import DAWidget


class MainWidget(qtw.QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setCentralWidget(DAWidget())
        self.setWindowTitle('Herramienta DAQ')
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWidget()

    sys.exit(app.exec())
