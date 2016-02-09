"""
Autor: Paul Kalauner 5BHIT
"""
from PySide.QtCore import SIGNAL
from PySide.QtGui import *

import CsvExampleView
from CsvExampleModel import CsvExampleModel
from CsvTableModel import CsvTableModel


class CsvExampleController(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_value = 0

        self.form = CsvExampleView.Ui_Form()
        self.form.setupUi(self)

        self.model = CsvExampleModel()
        self.table_model = CsvTableModel(self, self.model.data_list)
        self.form.contentTable.setModel(self.table_model)
        self.form.bReadFile.clicked.connect(self.read_file)

    def read_file(self):
        self.model.read_file()
        self.table_model.generate_headers()
        self.table_model.reset()
