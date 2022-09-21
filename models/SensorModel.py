class SensorModel():
    def __init__(self) -> None:
        self._sensors = ["GyroX", "GyroY", "GyroZ", "AccelX", "AccelY", "AccelZ"] 
        

    @property
    def sensors(self):
        return self._sensors