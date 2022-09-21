from abc import ABC, abstractmethod
from distutils.cmd import Command
from arduino.ArduinoSerial import ArduinoSerial
from typing import List

class ArduinoSensor(ABC):
    def __init__(self, command: str) -> None:
        self._command = command
    
    @property
    def command(self) -> str:
        return self._command

    @command.setter
    def command(self, value: str) -> None:
        if(value):
            self._command = value

    def getValue(self, port: ArduinoSerial) -> List[float]:
        try:
            if not port.is_open:
                port.open()
            
            port.writeLine(self._command)
            data = port.readLine().split(' ')

            return data
        except:
            print('Ocurrio un error, revisa la conexión.')