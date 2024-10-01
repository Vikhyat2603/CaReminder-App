# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainDesign(object):
    def setupUi(self, mainDesign):
        mainDesign.setObjectName("mainDesign")
        mainDesign.resize(900, 800)
        self.centralwidget = QtWidgets.QWidget(mainDesign)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(240, 20, 420, 70))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(240, 110, 420, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.addPatientButton = QtWidgets.QPushButton(self.centralwidget)
        self.addPatientButton.setGeometry(QtCore.QRect(300, 680, 300, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.addPatientButton.setFont(font)
        self.addPatientButton.setObjectName("addPatientButton")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(25, 180, 840, 480))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.table.setFont(font)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        mainDesign.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainDesign)
        self.statusbar.setObjectName("statusbar")
        mainDesign.setStatusBar(self.statusbar)

        self.retranslateUi(mainDesign)
        QtCore.QMetaObject.connectSlotsByName(mainDesign)

    def retranslateUi(self, mainDesign):
        _translate = QtCore.QCoreApplication.translate
        mainDesign.setWindowTitle(_translate("mainDesign", "Patients Window"))
        self.label.setText(_translate("mainDesign", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">MedNote</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("mainDesign", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; text-decoration: underline;\">Patients</span></p></body></html>"))
        self.addPatientButton.setText(_translate("mainDesign", "Add New Patient"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainDesign = QtWidgets.QMainWindow()
    ui = Ui_mainDesign()
    ui.setupUi(mainDesign)
    mainDesign.show()
    sys.exit(app.exec_())
