from utils.SingletonType import SingletonType
from arduino.ArduinoSensor import ArduinoSensor
from arduino.ArduinoSerial import ArduinoSerial
from reactivex.subject import Subject, BehaviorSubject


class SensorModel(ArduinoSensor, metaclass=SingletonType):
    def __init__(self, command, serial) -> None:
        super().__init__(command, serial)
        self._labels = ["GyroX", "GyroY",
                        "GyroZ", "AccelX", "AccelY", "AccelZ"]
        self.length = len(self._labels)
        self._command = command

        # Observables
        self.values_subject = Subject()
        self._is_open = BehaviorSubject(False)

    @property
    def labels(self):
        return self._labels

    @property
    def command(self):
        return self._command

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