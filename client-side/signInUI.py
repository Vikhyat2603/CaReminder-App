# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signInUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signInDesign(object):
    def setupUi(self, signInDesign):
        signInDesign.setObjectName("signInDesign")
        signInDesign.resize(900, 800)
        self.centralwidget = QtWidgets.QWidget(signInDesign)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(240, 20, 420, 70))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(240, 190, 420, 70))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(240, 340, 141, 70))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(240, 410, 151, 70))
        self.label_4.setObjectName("label_4")
        self.signInButton = QtWidgets.QPushButton(self.centralwidget)
        self.signInButton.setGeometry(QtCore.QRect(365, 530, 170, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.signInButton.setFont(font)
        self.signInButton.setObjectName("signInButton")
        self.switchToSignUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.switchToSignUpButton.setGeometry(QtCore.QRect(250, 620, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.switchToSignUpButton.setFont(font)
        self.switchToSignUpButton.setObjectName("switchToSignUpButton")
        self.pwdInput = QtWidgets.QLineEdit(self.centralwidget)
        self.pwdInput.setGeometry(QtCore.QRect(390, 430, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pwdInput.setFont(font)
        self.pwdInput.setStyleSheet("lineedit-password-mask-delay: 750")
        self.pwdInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdInput.setObjectName("pwdInput")
        self.emailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.emailInput.setGeometry(QtCore.QRect(380, 360, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.emailInput.setFont(font)
        self.emailInput.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.emailInput.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.emailInput.setObjectName("emailInput")
        signInDesign.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(signInDesign)
        self.statusbar.setObjectName("statusbar")
        signInDesign.setStatusBar(self.statusbar)

        self.retranslateUi(signInDesign)
        QtCore.QMetaObject.connectSlotsByName(signInDesign)

    def retranslateUi(self, signInDesign):
        _translate = QtCore.QCoreApplication.translate
        signInDesign.setWindowTitle(_translate("signInDesign", "Sign In Window"))
        self.label.setText(_translate("signInDesign", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">MedNote</span></p></body></html>"))
        self.label_2.setText(_translate("signInDesign", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Sign in to your account:</span></p></body></html>"))
        self.label_3.setText(_translate("signInDesign", "<html><head/><body><p><span style=\" font-size:24pt;\">Email ID:</span></p></body></html>"))
        self.label_4.setText(_translate("signInDesign", "<html><head/><body><p><span style=\" font-size:24pt;\">Password:</span></p></body></html>"))
        self.signInButton.setText(_translate("signInDesign", "Sign In"))
        self.switchToSignUpButton.setText(_translate("signInDesign", "New here? Create Another Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signInDesign = QtWidgets.QMainWindow()
    ui = Ui_signInDesign()
    ui.setupUi(signInDesign)
    signInDesign.show()
    sys.exit(app.exec_())
