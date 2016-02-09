"""
Autor: Paul Kalauner 5BHIT
"""
from CsvExampleModel import CsvExampleModel


class CsvExampleController(object):
    def __init__(self):
        self.last_value = 0
        self.model = CsvExampleModel()

    def read_file(self):
        self.model.read_file("file.csv")
