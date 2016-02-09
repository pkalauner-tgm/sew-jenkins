"""
Autor: Paul Kalauner 5BHIT
"""
import sys
from CsvExampleController import CsvExampleController
from PySide.QtGui import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = CsvExampleController()
    c.show()
    sys.exit(app.exec_())
