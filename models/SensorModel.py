from utils.SingletonType import SingletonType
from arduino.ArduinoSensor import ArduinoSensor
from reactivex.subject import Subject, BehaviorSubject
from database.LabelsDB import LabelsDB


class SensorModel(ArduinoSensor, metaclass=SingletonType):
    def __init__(self, command, serial) -> None:
        super().__init__(command, serial)

        self.init_db()

        self._labels: BehaviorSubject = BehaviorSubject(self._labels_db.list())

        self.length = len(self._labels.value)
        self._command = command

        # Observables
        self.values_subject = Subject()
        self._is_open = BehaviorSubject(False)

    @property
    def labels(self):
        return self._labels

    @property
    def labels_model(self):
        return self._labels_db.model

    @property
    def port(self) -> str:
        return self._serial.port

    @port.setter
    def port(self, value: str):
        self._serial.port = value

    def subscribe_values(self, on_next, on_error=None, on_completed=None) -> Subject.subscribe:
        return self.values_subject.subscribe(on_next, on_error, on_completed)

    def subscribe_serial_connection(self, on_next, on_error=None, on_completed=None):
        return self._is_open.subscribe(on_next, on_error, on_completed)

    def read_value(self):
        data = super().read_value()
        self.values_subject.on_next(data)

    def toggle_serial_open(self):
        is_open = self._serial.toggle_serial_open()
        self._is_open.on_next(is_open)

    def close(self):
        self._serial.close()
        self._is_open.on_next(self._serial._is_open)

    def remove_label(self, index):
        self._labels_db.model.removeRow(index)

    def add_label(self):
        self._labels_db.model.insertRows(self.labels_model.rowCount(), 1)

    def init_db(self):
        self._labels_db = LabelsDB()

    def emit_labels(self):
        self._labels_db.model.select()
        labels = self._labels_db.list()
        self.labels.on_next(labels)
