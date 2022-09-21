from abc import ABC, abstractmethod
from distutils.cmd import Command
from arduino.ArduinoSerial import ArduinoSerial
from typing import List
import numpy as np
class ArduinoSensor(ABC):
    def __init__(self, command: str, serial: ArduinoSerial) -> None:
        self._command = command
        self._serial = serial
    
    @property
    def command(self) -> str:
        return self._command

    @command.setter
    def command(self, value: str) -> None:
        if(value):
            self._command = value
    @property
    def value(self) -> List[float]:
        try:            
            self._serial.writeLine(self._command)
            data = self._serial.readLine().split(' ')

            return np.array(data, dtype=np.float16) 
        except:
            print('Ocurrio un error, revisa la conexión.')