from typing import Any
from utils.SingletonType import SingletonType
from PyQt5.QtWidgets import QStatusBar

class DAQModel(metaclass=SingletonType):
    def __init__(self, status_bar: QStatusBar) -> None:
        self._status_bar = status_bar
      
