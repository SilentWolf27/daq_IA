from typing import Any
from utils.SingletonType import SingletonType
import numpy as np

class DAQModel(metaclass=SingletonType):
    def __init__(self) -> None:
        self._data = np.array([])
        self._labels = np.array([])

    def append(self, data: Any, label):
            try:
                label = int(label)
            except ValueError:
                pass
            finally:     
                self._data = np.append(self._data, data)
                self._labels = np.append(self._labels, label)
      

    def clear(self):
        self._data = np.array([])
        self._labels = np.array([])

    @property
    def data(self):
        return self._data