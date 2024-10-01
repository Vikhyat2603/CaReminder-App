# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medsUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_medsDesign(object):
    def setupUi(self, medsDesign):
        medsDesign.setObjectName("medsDesign")
        medsDesign.resize(900, 800)
        self.centralwidget = QtWidgets.QWidget(medsDesign)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(240, 20, 420, 70))
        self.label.setObjectName("label")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setEnabled(True)
        self.titleLabel.setGeometry(QtCore.QRect(30, 100, 661, 70))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setUnderline(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(25, 180, 850, 480))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.table.setFont(font)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(30, 30, 50, 50))
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(35, 35))
        self.backButton.setObjectName("backButton")
        self.addMedButton = QtWidgets.QPushButton(self.centralwidget)
        self.addMedButton.setGeometry(QtCore.QRect(300, 690, 300, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.addMedButton.setFont(font)
        self.addMedButton.setObjectName("addMedButton")
        self.clearTicksButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearTicksButton.setGeometry(QtCore.QRect(765, 120, 110, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clearTicksButton.setFont(font)
        self.clearTicksButton.setObjectName("clearTicksButton")
        self.saveReportButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveReportButton.setGeometry(QtCore.QRect(710, 120, 50, 50))
        self.saveReportButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveReportButton.setIcon(icon1)
        self.saveReportButton.setIconSize(QtCore.QSize(35, 35))
        self.saveReportButton.setObjectName("saveReportButton")
        medsDesign.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(medsDesign)
        self.statusbar.setObjectName("statusbar")
        medsDesign.setStatusBar(self.statusbar)

        self.retranslateUi(medsDesign)
        QtCore.QMetaObject.connectSlotsByName(medsDesign)

    def retranslateUi(self, medsDesign):
        _translate = QtCore.QCoreApplication.translate
        medsDesign.setWindowTitle(_translate("medsDesign", "Medicines Window"))
        self.label.setText(_translate("medsDesign", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">MedNote</span></p></body></html>"))
        self.titleLabel.setText(_translate("medsDesign", "Medicines"))
        self.addMedButton.setText(_translate("medsDesign", "Add New Medicine"))
        self.clearTicksButton.setText(_translate("medsDesign", "Clear Ticks"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    medsDesign = QtWidgets.QMainWindow()
    ui = Ui_medsDesign()
    ui.setupUi(medsDesign)
    medsDesign.show()
    sys.exit(app.exec_())
