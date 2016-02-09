"""
Autor: Paul Kalauner 5BHIT
"""
import sys
from CsvExampleController import CsvExampleController
from PySide.QtGui import QApplication

if __name__ == "__main__":
    c = CsvExampleController()
    c.read_file()
