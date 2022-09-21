from serial import Serial, SerialException
import re
from serial.tools.list_ports_windows import comports

class ArduinoSerial():
    def __init__(self, port: str = None, baudrate: int = 9600, timeout: float = 1) -> None:
        self._serial: Serial = Serial(port=port, baudrate=baudrate, timeout=timeout)

    @property
    def port(self) -> Serial:
        return self._serial.port

    @port.setter
    def port(self, value: str):
        if value:
            self._serial.setPort(value)

    @property
    def is_open(self) -> bool:
        return self._serial.is_open

    def open(self) -> None:
        self._serial.open()
       
    def readLine(self) -> str:
        return self._serial.readline().strip().decode('utf-8')

    def writeLine(self, data: str) -> None:
        return self._serial.write(f"{data}\n".encode('utf-8'))

    def test_connection(self) -> bool:
        try:
            if not self._serial.is_open:
                self.open()

            self.writeLine('test')
            data = self.readLine()
            return data == "OK"
        except:
            return False

    def close(self) -> None:
        self.writeLine('close')
        data = self.readLine()

        if data == "OK":
            self._serial.close() 
            return True
        return False

    @classmethod
    def port_list(self):
        ports = []
        for info in comports():
            port, desc, hwid = info
            ports.append(port)

        return ports

        