# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signUpUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signUpDesign(object):
    def setupUi(self, signUpDesign):
        signUpDesign.setObjectName("signUpDesign")
        signUpDesign.resize(900, 800)
        self.centralwidget = QtWidgets.QWidget(signUpDesign)
        self.centralwidget.setObjectName("centralwidget")
        self.signUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(365, 520, 170, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.signUpButton.setFont(font)
        self.signUpButton.setObjectName("signUpButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(240, 20, 420, 70))
        self.label.setObjectName("label")
        self.switchToSignInButton = QtWidgets.QPushButton(self.centralwidget)
        self.switchToSignInButton.setGeometry(QtCore.QRect(250, 610, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.switchToSignInButton.setFont(font)
        self.switchToSignInButton.setObjectName("switchToSignInButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(240, 160, 420, 70))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(230, 330, 151, 70))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(230, 260, 141, 70))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(230, 380, 131, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pwdInput = QtWidgets.QLineEdit(self.centralwidget)
        self.pwdInput.setGeometry(QtCore.QRect(380, 350, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pwdInput.setFont(font)
        self.pwdInput.setStyleSheet("lineedit-password-mask-delay: 750")
        self.pwdInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdInput.setObjectName("pwdInput")
        self.confirmPwdInput = QtWidgets.QLineEdit(self.centralwidget)
        self.confirmPwdInput.setGeometry(QtCore.QRect(370, 420, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.confirmPwdInput.setFont(font)
        self.confirmPwdInput.setStyleSheet("lineedit-password-mask-delay: 750")
        self.confirmPwdInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPwdInput.setObjectName("confirmPwdInput")
        self.emailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.emailInput.setGeometry(QtCore.QRect(370, 280, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.emailInput.setFont(font)
        self.emailInput.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.emailInput.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.emailInput.setObjectName("emailInput")
        signUpDesign.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(signUpDesign)
        self.statusbar.setObjectName("statusbar")
        signUpDesign.setStatusBar(self.statusbar)

        self.retranslateUi(signUpDesign)
        QtCore.QMetaObject.connectSlotsByName(signUpDesign)

    def retranslateUi(self, signUpDesign):
        _translate = QtCore.QCoreApplication.translate
        signUpDesign.setWindowTitle(_translate("signUpDesign", "Sign Up Window"))
        self.signUpButton.setText(_translate("signUpDesign", "Sign Up"))
        self.label.setText(_translate("signUpDesign", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">MedNote</span></p></body></html>"))
        self.switchToSignInButton.setText(_translate("signUpDesign", "Sign in to an existing account"))
        self.label_2.setText(_translate("signUpDesign", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Create an account:</span></p></body></html>"))
        self.label_4.setText(_translate("signUpDesign", "<html><head/><body><p><span style=\" font-size:24pt;\">Password:</span></p></body></html>"))
        self.label_3.setText(_translate("signUpDesign", "<html><head/><body><p><span style=\" font-size:24pt;\">Email ID:</span></p></body></html>"))
        self.label_5.setText(_translate("signUpDesign", "<html><head/><body><p><span style=\" font-size:20pt;\">Confirm<br/>Password:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signUpDesign = QtWidgets.QMainWindow()
    ui = Ui_signUpDesign()
    ui.setupUi(signUpDesign)
    signUpDesign.show()
    sys.exit(app.exec_())
