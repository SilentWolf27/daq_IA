from typing import Any
from models.SensorModel import SensorModel
from utils.SingletonType import SingletonType
import numpy as np

class DAQModel(metaclass=SingletonType):
    def __init__(self) -> None:
        model = SensorModel()
        self._data = np.empty((1, model.length), order='C')
        self._labels = np.array([])
        self._saving = False

    def append(self, data: Any, label):
            print(data)
            try:
                label = int(label)
            except ValueError:
                pass
            finally:     
                self._data = np.append(self._data, np.array([data]), axis=0)
                self._labels = np.append(self._labels, label)
      

    def clear(self):
        self._data = np.array([])
        self._labels = np.array([])

    def save(self, filename):
        print(filename)
        
    @property
    def data(self):
        return self._data

    @property
    def saving(self):
        return self._saving
    
    @saving.setter
    def saving(self, value: bool):
        self._saving = value