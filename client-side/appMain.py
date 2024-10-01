# File: appMain.py
import os
import sys
import re
import csv
import datetime
import appClient

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtMultimedia import QSound

# Run shell command to convert Qt Creator's .ui files to .py files that can be imported
os.system('python -m PyQt5.uic.pyuic -x signInUI.ui -o signInUI.py')
os.system('python -m PyQt5.uic.pyuic -x signUpUI.ui -o signUpUI.py')
os.system('python -m PyQt5.uic.pyuic -x medsUI.ui -o medsUI.py')
os.system('python -m PyQt5.uic.pyuic -x mainUI.ui -o mainUI.py')
os.system('python -m PyQt5.uic.pyuic -x editPatientDialogUI.ui -o editPatientDialogUI.py')
os.system('python -m PyQt5.uic.pyuic -x addMedDialogUI.ui -o addMedDialogUI.py')
os.system('python -m PyQt5.uic.pyuic -x saveReportDialogUI.ui -o saveReportDialogUI.py')

from signInUI import Ui_signInDesign
from signUpUI import Ui_signUpDesign
from medsUI import Ui_medsDesign
from mainUI import Ui_mainDesign
from editPatientDialogUI import Ui_editPatientDialog as editPatientDesign
from addMedDialogUI import Ui_addMedDialog as addMedDesign
from saveReportDialogUI import Ui_saveReport as saveReportDesign

#########################################################################################

class editPatientDialogClass(qtw.QDialog, editPatientDesign):
    def __init__(self, patientID, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.patientID = patientID
        self.patientRenamed = False
        self.patientDeleted = False

        patientName = [patient[1] for patient in patients if patient[0]==patientID][0]
        self.nameInput.setText(patientName)
        
        self.accepted.connect(self.checkForRename)
        self.deleteButton.clicked.connect(self.confirmDelete)

    def checkForRename(self):
        # Fetch name for patient with this patientID
        patientName = [patient[1] for patient in patients if patient[0]==self.patientID][0]
        inputName = self.nameInput.text()
        
        if inputName != patientName:
            self.patientRenamed = True
            
    def confirmDelete(self):
        qm = qtw.QMessageBox
        result = qm.question(self, '', 'Confirm delete?', qm.Yes|qm.No)

        if result == qm.Yes:
            self.patientDeleted = True
            self.reject()

class addMedDialogClass(qtw.QDialog, addMedDesign):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.okButton.clicked.connect(self.checkAccept)
        self.cancelButton.clicked.connect(self.close)

        self.medTimesSpinBox.valueChanged.connect(self.timesValChanged)
        self.success = False

    def timesValChanged(self, value):
        self.timeEdit2.setEnabled(value>1)
        self.timingLabel2.setEnabled(value>1)
        
        self.timeEdit3.setEnabled(value>2)
        self.timingLabel3.setEnabled(value>2)
        
    def checkAccept(self):
        if self.medNameInput.text().strip() == "":
            qtw.QMessageBox.critical(self, "Error", "Please type medicine name")
        else:
            medName = self.medNameInput.text()
            medQty = self.qtySpinBox.value()
            medQtyUnit = self.qtyUnitComboBox.currentText()
            notes = self.notesInput.toPlainText()
            medTimes = self.medTimesSpinBox.value()
            time1 = self.timeEdit1.time()
            time2 = self.timeEdit2.time()
            time3 = self.timeEdit3.time()

            self.success = True
            self.inputData = [medName, medQty, medQtyUnit, notes, medTimes, time1, time2, time3]
            self.close()

class editMedDialogClass(qtw.QDialog, addMedDesign):
    def __init__(self, medName, medQty, medQtyUnit, notes, time1, time2, time3,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.okButton.clicked.connect(self.checkAccept)
        self.cancelButton.clicked.connect(self.close)
        font = self.titleLabel.font()
        self.titleLabel.setText('Edit Medicine')
        self.titleLabel.setFont(font)

        self.medTimesSpinBox.valueChanged.connect(self.timesValChanged)
        self.edited = False
        self.deleted = False

        ## Add delete button
        self.deleteButton = qtw.QPushButton(self)
        self.deleteButton.setGeometry(qtc.QRect(90, 750, 81, 31))
        self.deleteButton.setText("Delete")
        self.deleteButton.clicked.connect(self.confirmDelete)

        self.medNameInput.setText(medName)
        self.qtySpinBox.setValue(medQty)
        self.qtyUnitComboBox.setCurrentText(medQtyUnit)
        self.notesInput.setPlainText(notes)

        medTimes = 3-[time1, time2, time3].count(None)
        self.medTimesSpinBox.setValue(medTimes)

        h, m = map(int, time1.split(':'))
        self.timeEdit1.setTime(qtc.QTime(h, m))
        if time2:
            h, m = map(int, time2.split(':'))
            self.timeEdit2.setTime(qtc.QTime(h, m))
        if time3:
            h, m = map(int, time3.split(':'))
            self.timeEdit3.setTime(qtc.QTime(h, m))

    def timesValChanged(self, value):
        self.timeEdit2.setEnabled(value>1)
        self.timingLabel2.setEnabled(value>1)
        
        self.timeEdit3.setEnabled(value>2)
        self.timingLabel3.setEnabled(value>2)
        
    def checkAccept(self):
        if self.medNameInput.text().strip() == "":
            qtw.QMessageBox.critical(self, "Error", "Please type medicine name")
        else:
            medName = self.medNameInput.text()
            medQty = self.qtySpinBox.value()
            medQtyUnit = self.qtyUnitComboBox.currentText()
            notes = self.notesInput.toPlainText()
            medTimes = self.medTimesSpinBox.value()
            time1 = self.timeEdit1.time()
            time2 = self.timeEdit2.time()
            time3 = self.timeEdit3.time()

            self.edited = True
            # name, qty, unit, notes, no. times, 1st timing, 2nd timing, 3rd timing
            self.inputData = [medName, medQty, medQtyUnit, notes, medTimes, time1, time2, time3]
            self.close()

    def confirmDelete(self):
        qm = qtw.QMessageBox
        result = qm.question(self, '', 'Confirm delete?', qm.Yes|qm.No)

        if result == qm.Yes:
            self.deleted = True
            self.close()

class saveReportDialogClass(qtw.QDialog, saveReportDesign):
    def __init__(self, patientID, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.patientID = patientID
        self.saved = False
        
        patientName = [patient[1] for patient in patients if patient[0]==self.patientID][0]
        sheetName = patientName + " " + str(datetime.datetime.now().date())
        sheetName = patientName + " 2022-03-24" ##

        self.filenameInput.setText(sheetName)
        
        self.accepted.connect(self.saveReport)

    def saveReport(self):
        filename = self.filenameInput.text()

        path = f'.\\Saved Reports\\{filename}.csv'

        try:
            fileExists = os.path.isfile(path)
            if fileExists:
                qm = qtw.QMessageBox
                result = qm.question(self, '', 'Filename already in use, would you like to overwrite?', qm.Yes|qm.No)
                if result == qm.No:
                    qtw.QMessageBox.critical(self, "Error", "Filename already in use, not overwritten!")
                    return

            if ("\\" in filename) or ("/" in filename):
                raise Exception("Invalid filename")
            
            os.makedirs(os.path.dirname(path), exist_ok=True)
            file = open(path, 'w', newline='')
            writer = csv.writer(file)
            headers = ["MedID", "MedName", "MedQty", "MedQtyUnit", "Notes", "Time1", "Time2", "Time3", "wasTaken1", "wasTaken2", "wasTaken3", "patientID"]
            writer.writerows([headers])
            writer.writerows([med for med in meds if med[-1]==self.patientID])
            file.close()

            qtw.QMessageBox.information(self, "Success", "File Saved!")
            self.saved = True
            
        except Exception as e:
            qtw.QMessageBox.critical(self, "Error", "Error saving file: please choose a valid file name")
            
#########################################################################################

class mainWindowClass(qtw.QMainWindow, Ui_mainDesign):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        
        table = self.table
        self.table.setColumnCount(3)
        self.table.setRowCount(len(patients))
        self.table.setHorizontalHeaderLabels(['Patient', 'Medicines', 'Edit'])
        self.table.setEditTriggers(qtw.QTableWidget.NoEditTriggers)
        self.table.setSelectionMode(qtw.QTableWidget.NoSelection)
        self.table.setWordWrap(True)
        self.table.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOn)
        
        for rowID, patient in enumerate(patients):
            self.addPatientRow(rowID, patient[0], patient[1])

        self.addPatientButton.clicked.connect(self.addPatient)
        
        self.table.setColumnWidth(0, 340)
        self.table.setColumnWidth(1, 220)
        self.table.setColumnWidth(2, 220)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, qtw.QHeaderView.Fixed)
        header.setSectionResizeMode(1, qtw.QHeaderView.Fixed)
        header.setSectionResizeMode(2, qtw.QHeaderView.Fixed)
        
        self.table.resizeRowsToContents()
        vertHeader = self.table.verticalHeader()
        for row in range(len(patients)):
            vertHeader.setSectionResizeMode(row, qtw.QHeaderView.Fixed)
        
    def addPatientRow(self, rowID, patientID, patientName):
        nameLabel = qtw.QTableWidgetItem(patientName)
        nameLabel.setFont(qtg.QFont('Time', 20))
                    
        medsButton = qtw.QPushButton('', self)
        editButton = qtw.QPushButton('', self)
        
        medsButton.setIcon(qtg.QIcon(assetPaths['medsIcon']))
        medsButton.clicked.connect(lambda x, p=patientID: self.viewPatientMeds(p))
        editButton.setIcon(qtg.QIcon(assetPaths['editIcon']))
        editButton.clicked.connect(lambda x, p=patientID, r=rowID:self.editPatient(p,r))

        medsButton.setIconSize(qtc.QSize(50,50))
        editButton.setIconSize(qtc.QSize(45,45))

        self.table.setItem(rowID, 0, nameLabel)
        self.table.setCellWidget(rowID, 1, medsButton)
        self.table.setCellWidget(rowID, 2, editButton)

    def editPatient(self, patientID, rowID):
        global patients
        editDialog = editPatientDialogClass(patientID)
        editDialog.exec_()
        renamed = editDialog.patientRenamed
        deleted = editDialog.patientDeleted
        if renamed:
            patientName = editDialog.nameInput.text()
            if patientName.strip() == "":
                qtw.QMessageBox.critical(self, "Error", "Please type patient name")
            else:
                response = appClient.renamePatient(userEmail, userPassword, patientName, patientID)
                
                if not response['status']:
                    qtw.QMessageBox.critical(self, "Error", response['result'])
                    
                else:
                    index = [i for i in range(len(patients)) if patients[i][0]==patientID][0]
                    patients[index][1] = patientName

                    self.table.item(rowID, 0).setText(patientName)
                    
                    self.table.resizeRowsToContents()
                
        elif deleted:
            response = appClient.deletePatient(userEmail, userPassword, patientID)
            
            if not response['status']:
                qtw.QMessageBox.critical(self, "Error", response['result'])
                
            else:
                index = [i for i in range(len(patients)) if patients[i][0]==patientID][0]
                del patients[index]                
                
                self.table.removeRow(rowID)


    def addPatient(self):
        patientName, okPressed = qtw.QInputDialog.getText(self, "Add Patient", "Patient name:")
        
        if okPressed:

            # Ensures patient name is not blank value
            if patientName.strip() == "":
                qtw.QMessageBox.critical(self, "Error", "Please type patient name")

            # Ensures patientName does not already exist under user
            elif patientName.strip() in [p[1] for p in patients]:
                qtw.QMessageBox.critical(self, "Error", "Patient name already exists")
                
            else:
                response = appClient.addPatient(userEmail, userPassword, patientName)
                if not response['status']:
                    qtw.QMessageBox.critical(self, "Error", response['result'])
                
                else:
                    patientID = response['result']
                    patients.append([patientID, patientName])

                    rowID = mainWindow.table.rowCount()
                    self.table.setRowCount(rowID+1)
                    self.addPatientRow(rowID, patientID, patientName)
                    self.table.resizeRowsToContents()

    def viewPatientMeds(self, patientID):
        global medsWindow
        
        medsWindow = medsWindowClass(patientID)
        medsWindow.show()
        self.close()
 
#######################################################################################

class medsWindowClass(qtw.QMainWindow, Ui_medsDesign):
    def __init__(self, patientID, *args, **kwargs):        
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.patientID = patientID
        self.meds = [med for med in meds if med[-1] == patientID]

        self.table.setEditTriggers(qtw.QTableWidget.NoEditTriggers)
        self.table.setSelectionMode(qtw.QTableWidget.NoSelection)
        self.table.setWordWrap(True)
        self.table.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOn)
        
        patientName = [patient[1] for patient in patients if patient[0] == patientID][0]
        self.titleLabel.setText(f'Medicines for {patientName}')

        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['Medicine', 'Quantity', 'Time', 'Info', 'Edit', 'Taken'])
        
        self.addMedButton.clicked.connect(self.addMedicine)
        self.backButton.clicked.connect(self.backToPatients)
        self.backButton.setIcon(qtg.QIcon(assetPaths['backIcon']))

        self.clearTicksButton.clicked.connect(self.clearTicks)
        self.saveReportButton.clicked.connect(self.saveReport)
        self.saveReportButton.setIcon(qtg.QIcon(assetPaths['reportIcon']))

        columnWidths = [275, 150, 120, 80, 80, 80]
        for i, width in enumerate(columnWidths):
            self.table.setColumnWidth(i, width)

        self.populateTable()

        horizHeader = self.table.horizontalHeader()
        for col in range(5):
            horizHeader.setSectionResizeMode(col, qtw.QHeaderView.Fixed)
        
    def populateTable(self):
        # Set row count to 0 to clear medicine timing records
        self.table.setRowCount(0)

        # Set row count to maximum number possible: no. of meds X 3
        medCount = len(self.meds)
        self.table.setRowCount(medCount*3)

        # Create a list to store all the medicine timing entries to be shown
        medTimings = []

        # Iterate through this patient's medicines
        for med in self.meds:

            # Iterate through 3 possible timing indices (0-time1, 1-time2, 2-time3)
            for timingNumber in range(3):
                # Fetch the corresponding time column [index 5,6,7] of the med row 
                time = med[timingNumber + 5]
                
                # Break loop if the time value stored for this timingNumber is None
                if time == None:
                    break

                # Append tuple: (row of med details, timingNumber [0, 1, or 2], corresponding time value
                medTimings.append((med, timingNumber, time))

        # The tuples are sorted by the time value (last element of the tuple)
        medTimings.sort(key=lambda x:x[-1])

        # Use enumerate to get a loop counter rowID while also iterating through the list elements
        for rowID, (med, timingIndex, time) in enumerate(medTimings):
            # Call addMedRow method with parameter [rowID, medID, medName, medQty, and timingIndex]
            self.addMedRow(rowID, med[0], med[1], med[2], med[3], timingIndex)

        # Resize table to have as many rows as there are total medicine timings
        self.table.setRowCount(len(medTimings))

        # Resize and fix table row heights
        self.table.resizeRowsToContents()
        vertHeader = self.table.verticalHeader()
        for row in range(self.table.rowCount()):
            vertHeader.setSectionResizeMode(row, qtw.QHeaderView.Fixed)

    def addMedRow(self, rowID, medID, medName, qty, qtyUnit, timingIndex):
        nameLabel = qtw.QTableWidgetItem(medName)
        nameLabel.setFont(qtg.QFont('Time', 20))

        med = [m for m in self.meds if m[0]==medID][0]
        qtyText = qtw.QTableWidgetItem(str(qty) + ' ' + str(qtyUnit))
        timeText = qtw.QTableWidgetItem(med[timingIndex+5])

        qtyText.setTextAlignment(qtc.Qt.AlignCenter)
        timeText.setTextAlignment(qtc.Qt.AlignCenter)
                    
        notesButton = qtw.QPushButton('', self)
        notesButton.setIcon(qtg.QIcon(assetPaths['infoIcon']))
        notesButton.setIconSize(qtc.QSize(50,50))
        notesButton.clicked.connect(lambda: self.showNotes(medID))

        editButton = qtw.QPushButton('', self)
        editButton.setIcon(qtg.QIcon(assetPaths['editIcon']))
        editButton.setIconSize(qtc.QSize(50,50))
        editButton.clicked.connect(lambda: self.editMedicine(medID))

        tickButton = qtw.QPushButton('✓', self)
        tickButton.clicked.connect(lambda: self.tickMedicineTiming(medID, timingIndex, rowID))
        
        self.table.setItem(rowID, 0, nameLabel)
        self.table.setItem(rowID, 1, qtyText)
        self.table.setItem(rowID, 2, timeText)
        self.table.setCellWidget(rowID, 3, notesButton)
        self.table.setCellWidget(rowID, 4, editButton)
        self.table.setCellWidget(rowID, 5, tickButton)

        if med[timingIndex+8]:
            for j in range(3):
                item = self.table.item(rowID,j)
                f = item.font()
                f.setStrikeOut(True)
                item.setFont(f)

    def showNotes(self, medID):
        notes = [row[4] for row in self.meds if row[0]==medID][0]
        qtw.QMessageBox.information(self, "Notes", notes)        

    def addMedicine(self):        
        addMedDialog = addMedDialogClass()
        addMedDialog.exec_()

        if addMedDialog.success:
            medName, medQty, medQtyUnit, notes, medTimes, time1, time2, time3 = addMedDialog.inputData

            time1 = time1.toString()[:-3]
            time2 = time2.toString()[:-3]
            time3 = time3.toString()[:-3]

            if medTimes == 1:
                time2 = None
                time3 = None
                
            elif medTimes == 2:
                time1, time2 = sorted([time1, time2])
                time3 = None

            else:
                time1, time2, time3 = sorted([time1, time2, time3])
                
            response = appClient.addMed(userEmail, userPassword, medName, medQty,
                             medQtyUnit, notes, time1, time2, time3, self.patientID)

            if not response['status']:
                qtw.QMessageBox.critical(self, "Error", response['result'])
            else:
                medID = response['result']

                row = [medID, medName, medQty, medQtyUnit, notes, time1,
                       time2, time3, 0, 0, 0, self.patientID]

                self.meds.append(row)
                meds.append(row)

                self.populateTable()

    def editMedicine(self, medID):
        med = [m for m in self.meds if m[0]==medID][0]
        
        medID, medName, medQty, medQtyUnit, notes, time1,\
                   time2, time3, wasTaken1, wasTaken2, wasTaken3 = med[:11]

        editMedDialog = editMedDialogClass(medName, medQty, medQtyUnit, notes, time1,
                                           time2, time3)
        
        editMedDialog.exec_()

        if editMedDialog.edited:
            medName, medQty, medQtyUnit, notes, medTimes, time1, time2, time3 = editMedDialog.inputData

            time1 = time1.toString()[:-3]
            time2 = time2.toString()[:-3]
            time3 = time3.toString()[:-3]

            if medTimes == 1:
                time2 = None
                time3 = None
                
            elif medTimes == 2:
                time1, time2 = sorted([time1, time2])
                time3 = None

            else:
                time1, time2, time3 = sorted([time1, time2, time3])

            if medTimes < 2:
                wasTaken2 = 0

            if medTimes < 3:
                wasTaken3 = 0                        
            
            response = appClient.editMed(userEmail, userPassword, medID, medName, medQty,
                             medQtyUnit, notes, time1, time2, time3, wasTaken1, wasTaken2, wasTaken3)

            if not response['status']:
                qtw.QMessageBox.critical(self, "Error", response['result'])
            else:
                row = [medID, medName, medQty, medQtyUnit, notes, time1,
                       time2, time3, wasTaken1, wasTaken2, wasTaken3, self.patientID]

                selfMedTableIndex = [i for i in range(len(self.meds)) if self.meds[i][0]==medID][0]
                del self.meds[selfMedTableIndex]

                medTableIndex = [i for i in range(len(meds)) if meds[i][0]==medID][0]
                del meds[medTableIndex]

                self.meds.append(row)
                meds.append(row)

                self.populateTable()
            
        elif editMedDialog.deleted:
            response = appClient.deleteMed(userEmail, userPassword, medID)
            if not response['status']:
                qtw.QMessageBox.critical(self, "Error", response['result'])
            else:
                del self.meds[[i for i in range(len(self.meds)) if self.meds[i][0]==medID][0]]
                del meds[[i for i in range(len(meds)) if meds[i][0]==medID][0]]

                self.populateTable()

    def tickMedicineTiming(self, medID, timingIndex, rowID):

        selfMedTableIndex = [i for i in range(len(self.meds)) if self.meds[i][0]==medID][0]
        newState = 1 - self.meds[selfMedTableIndex][timingIndex+8]
        
        response = appClient.tickMedTiming(userEmail, userPassword, medID, timingIndex, newState)
        
        if not response['status']:
            qtw.QMessageBox.critical(self, "Error", response['result'])
        else:
            
            selfMedTableIndex = [i for i in range(len(self.meds)) if self.meds[i][0]==medID][0]
            self.meds[selfMedTableIndex][timingIndex+8] = newState

            medTableIndex = [i for i in range(len(meds)) if meds[i][0]==medID][0]               
            meds[medTableIndex][timingIndex+8] = newState

            for j in range(3):
                item = self.table.item(rowID,j)
                f = item.font()
                f.setStrikeOut(newState)
                item.setFont(f)

    def clearTicks(self):
        qm = qtw.QMessageBox
        result = qm.question(self, '', 'Are you sure you want to clear the ticked status from all the medicines?', qm.Yes|qm.No)

        if result == qm.Yes:
            response = appClient.clearTicks(userEmail, userPassword, self.patientID)
            
            if not response['status']:
                qtw.QMessageBox.critical(self, "Error", response['result'])
            else:
                for med in self.meds:
                    med[8] = 0
                    med[9] = 0
                    med[10] = 0

                for med in meds:
                    if med[-1] == self.patientID:
                        med[8] = 0
                        med[9] = 0
                        med[10] = 0

                for row in range(self.table.rowCount()):
                    for j in range(3):
                        item = self.table.item(row,j)
                        f = item.font()
                        f.setStrikeOut(0)
                        item.setFont(f)

    def saveReport(self):
        saveReportDialog = saveReportDialogClass(self.patientID)
        saveReportDialog.exec_()
                        
    def backToPatients(self):
        mainWindow.show()
        self.close()

#######################################################################################
        
class signInWindowClass(qtw.QMainWindow, Ui_signInDesign):
    global response
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # inherits features from the parent classes
        self.setupUi(self) # creates design elements

        # Bind the buttons to class methods
        self.switchToSignUpButton.clicked.connect(self.switchToSignUpWindow)
        self.signInButton.clicked.connect(self.signInPressed)
        
##        ## ONLY FOR TESTING
##        self.emailInput.setText('test1@gmail.com')
##        self.pwdInput.setText('test1pwd')

    def switchToSignUpWindow(self):
        # Show the sign-up window and close this window
        signUpWindow.show()
        self.close()

    def signInPressed(self):
        global userEmail, userPassword, mainWindow

        # Fetch email and password typed in UI input boxes
        userEmail = self.emailInput.text()
        userPassword = self.pwdInput.text()

        # Use RegEx to ensure email is of a valid format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", userEmail):
            qtw.QMessageBox.critical(self, "Error", "Invalid email!")  
            return

        # Send request to server to login
        response = appClient.loginUser(userEmail, userPassword)

        # Check if server returned an error
        if not response['status']:
            qtw.QMessageBox.critical(self, "Error", response['result'])
        else:
            # Initialise and show the main screen, close this window
            mainWindow = initialiseMainScreen(userEmail, userPassword)
            mainWindow.show()
            self.close()
            
#######################################################################################

class signUpWindowClass(qtw.QMainWindow, Ui_signUpDesign):
    global response
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.switchToSignInButton.clicked.connect(self.switchToSignInWindow)
        self.signUpButton.clicked.connect(self.signUpPressed)

    def switchToSignInWindow(self):
        signInWindow.show()
        self.close()

    def signUpPressed(self):
        global userEmail, userPassword, mainWindow

        # Fetch email and password and confirmPassword typed in UI input boxes
        userEmail = self.emailInput.text()
        userPassword = self.pwdInput.text()
        userConfirmPassword = self.confirmPwdInput.text()

        # Ensure that user has typed the same password again for confirm password
        if userPassword != userConfirmPassword:
            qtw.QMessageBox.critical(self, "Error", "Passwords don't match!")
            return

        # Use RegEx to ensure email is of a valid format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", userEmail):
            qtw.QMessageBox.critical(self, "Error", "Invalid e-mail!")
            return

        # Ensure that user password length is at least 8 characters
        if len(userPassword)<8:
            qtw.QMessageBox.critical(self, "Error", "Password should be at least 8 characters!")
            return

        response = appClient.registerUser(userEmail, userPassword)

        if not response['status']:
            qtw.QMessageBox.critical(self, "Error", response['result'])
        else:
            mainWindow = initialiseMainScreen(userEmail, userPassword)
            mainWindow.show()
            self.close()

#######################################################################################

def excepthook(exc_type, exc_value, exc_tb):
    ## Quit app in case of any errors in the code
    app.quit()
    raise Exception(exc_type, exc_value, exc_tb)    

def initialiseMainScreen(userEmail, userPassword):
    global patients, meds

    response = appClient.fetchData(userEmail, userPassword)
        
    if response['status']:    
        patients, meds = response['result']        
        return mainWindowClass()

    else:
        qtw.QMessageBox.critical(self, "Error", response['result'])
    
if __name__ == '__main__':
    sys.excepthook = excepthook
    
    qtw.QApplication.setStyle('Oxygen')
    app = qtw.QApplication([])
    
    errorSound = QSound(r".\assets\error.wav")

    ## File paths for icons to  be used in user interface
    assetPaths = {'medsIcon' : r'.\assets\meds.png',
              'editIcon' : r'.\assets\edit.png',
              'backIcon': r'.\assets\back.png',
              'infoIcon': r'.\assets\info.png',
              'reportIcon': r'.\assets\report.png'}

    ## Instantiate the sign in and sign up windows so they can be switched between if needed
    signInWindow = signInWindowClass()
    signUpWindow = signUpWindowClass()
    signInWindow.show()
    
    sys.exit(app.exec_())
