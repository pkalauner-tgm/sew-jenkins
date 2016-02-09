# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Paul\Dropbox\Schule\SEW\Python_Projects\csv_example\CsvExampleView.ui'
#
# Created: Tue Jan 12 14:21:39 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.contentTable = QtGui.QTableView(Form)
        self.contentTable.setObjectName("contentTable")
        self.verticalLayout.addWidget(self.contentTable)
        self.bReadFile = QtGui.QPushButton(Form)
        self.bReadFile.setObjectName("bReadFile")
        self.verticalLayout.addWidget(self.bReadFile)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "CSV-Example", None, QtGui.QApplication.UnicodeUTF8))
        self.bReadFile.setText(QtGui.QApplication.translate("Form", "Read file.csv", None, QtGui.QApplication.UnicodeUTF8))

