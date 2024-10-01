# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editPatientDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editPatientDialog(object):
    def setupUi(self, editPatientDialog):
        editPatientDialog.setObjectName("editPatientDialog")
        editPatientDialog.resize(350, 283)
        self.buttonBox = QtWidgets.QDialogButtonBox(editPatientDialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 220, 161, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(editPatientDialog)
        self.label.setGeometry(QtCore.QRect(100, 15, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(editPatientDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.nameInput = QtWidgets.QLineEdit(editPatientDialog)
        self.nameInput.setGeometry(QtCore.QRect(100, 90, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nameInput.setFont(font)
        self.nameInput.setText("")
        self.nameInput.setObjectName("nameInput")
        self.deleteButton = QtWidgets.QPushButton(editPatientDialog)
        self.deleteButton.setGeometry(QtCore.QRect(90, 160, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")

        self.retranslateUi(editPatientDialog)
        self.buttonBox.accepted.connect(editPatientDialog.accept)
        self.buttonBox.rejected.connect(editPatientDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(editPatientDialog)

    def retranslateUi(self, editPatientDialog):
        _translate = QtCore.QCoreApplication.translate
        editPatientDialog.setWindowTitle(_translate("editPatientDialog", "Edit Patient"))
        self.label.setText(_translate("editPatientDialog", "Edit Patient"))
        self.label_2.setText(_translate("editPatientDialog", "Name:"))
        self.deleteButton.setText(_translate("editPatientDialog", "Delete Patient"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editPatientDialog = QtWidgets.QDialog()
    ui = Ui_editPatientDialog()
    ui.setupUi(editPatientDialog)
    editPatientDialog.show()
    sys.exit(app.exec_())
