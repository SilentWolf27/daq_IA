from utils.SingletonType import SingletonType


class SensorModel(metaclass=SingletonType):
    def __init__(self) -> None:
        self._sensors = ["GyroX", "GyroY", "GyroZ", "AccelX", "AccelY", "AccelZ"] 
        self.length = len(self._sensors)
        self._command = 'G'

    @property
    def sensors(self):
        return self._sensors
    
    @property
    def command(self):
        return self._command

