from PyQt5 import QtWidgets as qtw
from models.StatusModel import StatusModel

class StatusWidget(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()

        main_layout = qtw.QHBoxLayout()

        self.port_status = qtw.QLabel()
        self.port_status.setText("")
        main_layout.addWidget(self.port_status)
        main_layout.addStretch()

        self.data_status = qtw.QLabel()
        self.data_status.setText("")
        main_layout.addWidget(self.data_status)

        self.setLayout(main_layout)

        status_model = StatusModel()
        self.port_status_sub = status_model.port_status.subscribe(self.on_port_change)
        self.port_status_sub = status_model.data_status.subscribe(self.on_daq_change)

    def on_port_change(self, value): 
        self.port_status.setText(value)

    def on_daq_change(self, value): 
        self.data_status.setText(value)