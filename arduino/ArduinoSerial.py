from serial import Serial, SerialException
import re
from serial.tools.list_ports import comports


class ArduinoSerial():
    def __init__(self, port: str = None, baudrate: int = 9600, timeout: float = 1) -> None:
        self._serial: Serial = Serial(
            port=port, baudrate=baudrate, timeout=timeout)

        self._is_open = False

    @property
    def serial(self) -> Serial:
        return self._serial

    @property
    def port(self) -> str:
        return self._serial.port

    @port.setter
    def port(self, value: str):
        if self._serial.is_open:
            self._serial.close()

        if value:
            self._serial.setPort(value)
            self._serial.open()

    @property
    def is_open(self) -> bool:
        return self._is_open

    def safe_open(self) -> bool:
        try:
            if not self._serial.is_open:
                self._serial.open()

            self.writeLine('open')
            data = self.readLine()

            if data == "OK":
                self._is_open = True
                return True
            else:
                self.is_open = False
                return self._is_open
        except:
            self._is_open = False
            return self._is_open

    def readLine(self) -> str:
        return self._serial.readline().strip().decode('utf-8')

    def writeLine(self, data: str) -> None:
        return self._serial.write(f"{data}\n".encode('utf-8'))

    def safe_close(self) -> None:
        self.writeLine('close')
        data = self.readLine()

        if data == "OK":
            self._serial.close()
            self._is_open = False
            self._serial.port = None
            return self._is_open
            
        self._is_open = True    
        return self._is_open

    @classmethod
    def port_list(self):
        ports = []
        for info in comports():
            port, desc, hwid = info
            ports.append(port)

        return ports

    def toggle_serial_open(self):
        if self._is_open:
            return self.safe_close() 
        else:
            return self.safe_open() 

    def close(self):
        self._serial.close()

class ArduinoConnectionException(Exception):
    pass