"""
Autor: Rene Hollander, Paul Kalauner 5BHIT
"""
from PySide.QtCore import QAbstractTableModel, Qt


class CsvTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = []
        self.generate_headers()

    def generate_headers(self):
        if len(self.mylist) > 0:
            for key in self.mylist[0]:
                self.header.append(key)

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.header)

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][self.header[index.column()]]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
