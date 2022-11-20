from arduino.ArduinoSerial import ArduinoSerial
from typing import List
import numpy as np


class ArduinoSensor():
    def __init__(self, command: str, serial: ArduinoSerial) -> None:
        self._command = command
        self._serial = serial
        self._value = np.array([])

    @property
    def command(self) -> str:
        return self._command

    @command.setter
    def command(self, value: str) -> None:
        if (value):
            self._command = value

    @property
    def value(self) -> List[float]:
        return self._value

    def read_value(self) -> List[float]:
        return np.random.randint(0, 100, size=(6, ))
        try:
            self._serial.writeLine(self._command)
            data = self._serial.readLine().split(' ')

            self._value = np.array(data, dtype=np.float16)
            return self._value
        except:
            print('Ocurrio un error, revisa la conexión.')

    