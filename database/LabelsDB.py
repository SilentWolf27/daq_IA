from PyQt5 import QtSql as qts
from database.db import DB
import sys
from PyQt5 import QtCore as qtc


class LabelsDB(DB):
    def __init__(self) -> None:
        super().__init__()
        self.db.open()
        self.model = qts.QSqlTableModel(None, self.db)
        self.model.setTable('labels')
        self.model.setHeaderData(1, qtc.Qt.Horizontal, 'Nombre')
        self.model.select()

    def list(self):
        labels = []
        query = qts.QSqlQuery('SELECT name FROM labels', self.db)
        query.exec()
        while query.next():
            labels.append(query.value('name'))

        return labels
