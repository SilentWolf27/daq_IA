from PyQt5 import QtSql as qts
from PyQt5 import QtWidgets as qtw
import sys
from utils.SingletonType import SingletonType


class DB(metaclass=SingletonType):
    def __init__(self) -> None:
        self.db = qts.QSqlDatabase('QSQLITE')
        self.db.setDatabaseName('sensor.db')

        if not self.db.open():
            error = self.db.lastError().text()

            qtw.QMessageBox.critical(
                None, 'DB Connection Error', 'Could not open database file: 'f'{error}')
            sys.exit(1)