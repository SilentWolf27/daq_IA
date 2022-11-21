from typing import Any
from utils.SingletonType import SingletonType
from reactivex.subject import BehaviorSubject


class StatusModel(metaclass=SingletonType):
    def __init__(self) -> None:
        self._port_status_sub = BehaviorSubject('Puerto serie desconectado')
        self._error_sub = BehaviorSubject('')
        self._data_status_sub = BehaviorSubject(
            'Adquisición de datos detenida: 0 datos guardados')

    @property
    def port_status(self):
        return self._port_status_sub

    @port_status.setter
    def port_status(self, value):
        if isinstance(value, str):
            self._port_status_sub.on_next(value)

    @property
    def data_status(self):
        return self._data_status_sub

    @data_status.setter
    def data_status(self, value):
        if isinstance(value, str):
            self._data_status_sub.on_next(value)

    @property
    def error(self):
        return self._error_sub

    @error.setter
    def error(self, value):
        if isinstance(value, str):
            self._error_sub.on_next(value)
