from typing import Any
from models.SensorModel import SensorModel
from utils.SingletonType import SingletonType
import numpy as np
import pandas as pd
from reactivex.subject import BehaviorSubject


class DAQModel(metaclass=SingletonType):
    def __init__(self) -> None:
        model = SensorModel()
        self._data = np.empty((0, model.length))
        self._labels = np.array([], dtype=np.int8)
        self._is_saving_subject = BehaviorSubject(False)
        self.is_saving = False

    def append(self, data: Any, label):
        try:
            label = int(label)
        except ValueError:
            pass
        finally:
            self._data = np.append(self._data, np.array([data]), axis=0)
            self._labels = np.append(self._labels, label)

    def clear(self):
        model = SensorModel()
        self._data = np.empty((0, model.length))
        self._labels = np.array([])

    def save(self, filename):
        sensor_model = SensorModel()
        output = pd.DataFrame(self._data, columns=sensor_model.values)
        output['Output'] = self._labels

        output.to_csv(filename, index=False)

    def subscribe_data_saving(self, on_next, on_error=None, on_completed=None):
        return self._is_saving_subject.subscribe(on_next, on_error, on_completed)

    @property
    def data(self):
        return self._data

    @property
    def saving(self):
        return self.is_saving

    @saving.setter
    def saving(self, value: bool):
        self._saving = value

    def toggle_save(self):
        self.is_saving = not self.is_saving
        self._is_saving_subject.on_next(self.is_saving)

    @property
    def length(self):
        h, _ = self.data.shape
        return h