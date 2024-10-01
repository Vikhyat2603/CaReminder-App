# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saveReportDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_saveReport(object):
    def setupUi(self, saveReport):
        saveReport.setObjectName("saveReport")
        saveReport.resize(350, 266)
        self.buttonBox = QtWidgets.QDialogButtonBox(saveReport)
        self.buttonBox.setGeometry(QtCore.QRect(70, 200, 181, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(saveReport)
        self.label.setGeometry(QtCore.QRect(10, 10, 321, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(saveReport)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.filenameInput = QtWidgets.QLineEdit(saveReport)
        self.filenameInput.setGeometry(QtCore.QRect(90, 140, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.filenameInput.setFont(font)
        self.filenameInput.setText("")
        self.filenameInput.setObjectName("filenameInput")

        self.retranslateUi(saveReport)
        self.buttonBox.accepted.connect(saveReport.accept)
        self.buttonBox.rejected.connect(saveReport.reject)
        QtCore.QMetaObject.connectSlotsByName(saveReport)

    def retranslateUi(self, saveReport):
        _translate = QtCore.QCoreApplication.translate
        saveReport.setWindowTitle(_translate("saveReport", "Edit Patient"))
        self.label.setText(_translate("saveReport", "<html><head/><body><p>Do you want to save a report of the medicines taken?</p></body></html>"))
        self.label_2.setText(_translate("saveReport", "File Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    saveReport = QtWidgets.QDialog()
    ui = Ui_saveReport()
    ui.setupUi(saveReport)
    saveReport.show()
    sys.exit(app.exec_())
