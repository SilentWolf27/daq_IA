from PyQt5 import QtWidgets as qtw
from models.SensorModel import SensorModel
from PyQt5 import QtCore as qtc


class ConfigSensorWidget(qtw.QDialog):

    def __init__(self) -> None:
        super().__init__()
        self.settings = qtc.QSettings('IMT_UASLP', 'IA_DAQ')
        main_layout = qtw.QVBoxLayout()

        command_layout = qtw.QHBoxLayout()
        command_layout.addWidget(qtw.QLabel('Comando de lectura:'))
        self.command_input = qtw.QLineEdit(editingFinished=self.save_command)
        self.command_input.setText(
            self.settings.value('sensor/command', 'G', type=str))
        command_layout.setContentsMargins(0, 10, 0, 20)
        command_layout.addWidget(self.command_input)
        main_layout.addLayout(command_layout)

        main_layout.addWidget(qtw.QLabel('Valores del sensor'))
        self.sensor = SensorModel()
        self.label_list = qtw.QTableView()
        self.label_list.setModel(self.sensor.labels_model)
        self.label_list.setColumnHidden(0, 1)
        self.label_list.horizontalHeader().setSectionResizeMode(1, qtw.QHeaderView.Stretch)
        scrollarea = qtw.QScrollArea()
        scrollarea.setWidget(self.label_list)
        main_layout.addWidget(scrollarea)

        button_layout = qtw.QHBoxLayout()
        save_button = qtw.QPushButton('Eliminar', clicked=self.remove_item)
        close_button = qtw.QPushButton('Agregar', clicked=self.add_item)
        button_layout.addWidget(save_button)
        button_layout.addWidget(close_button)

        main_layout.addLayout(button_layout)
        self.setWindowTitle('Configurar sensor')
        self.setLayout(main_layout)

    def add_item(self):
        self.sensor.add_label()

    def remove_item(self):
        selected = self.label_list.selectedIndexes()

        for index in selected:
            self.sensor.remove_label(index.row())

    def save_command(self):
        self.settings.setValue('sensor/command', self.command_input.text())
