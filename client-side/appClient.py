# File: appClient.py
import requests
from cryptography.fernet import Fernet

key = bytes(open('credentials.txt', 'r').read(), 'utf-8')
my_cipher = Fernet(key)

##url = "http://127.0.0.1:5000"

url = "https://Vikhyat.pythonanywhere.com"

#################### Register ####################

def registerUser(userEmail, userPassword):
    global requestJson, r

    userPassword = my_cipher.encrypt(userPassword.encode('utf-8')).decode('utf-8')
    
    requestJson = {'instruction'     : 'registerUser',
            'userEmail'       : userEmail,        
            'userPassword'    : userPassword}

    r = requests.post(url, json=requestJson)
    return r.json()

###################### Login #####################
##    global requestJson, r

def loginUser(userEmail, userPassword):

    # Convert password into bytes object, encrypt it, and convert it back to a string
    userPassword = my_cipher.encrypt(userPassword.encode('utf-8')).decode('utf-8')

    # Create JSON containing instruction and credentials to be sent to server
    requestJson = {'instruction' : 'loginUser',
            'userEmail'   : userEmail,        
            'userPassword': userPassword}

    # Send a POST request to the server
    r = requests.post(url, json=requestJson)

    # Return JSON response from the server
    return r.json()

################### Fetch Data ###################

def fetchData(userEmail, userPassword):
    global requestJson, r

    userPassword = my_cipher.encrypt(userPassword.encode('utf-8')).decode('utf-8')
    
    requestJson = {'instruction'   : 'fetchData',
            'userEmail'     : userEmail,
            'userPassword'  : userPassword,
            'fields':[]}

    r = requests.post(url, json=requestJson)
    return r.json()

############## Primary DB Functions ##############

def addPatient(userEmail, userPassword, patientName):
    global requestJson, r

    userPassword = my_cipher.encrypt(userPassword.encode('utf-8')).decode('utf-8')
    
    requestJson = {'instruction' : 'addPatient',
            'userEmail'   : userEmail,        
            'userPassword': userPassword,
            'fields' : [patientName]}

    r = requests.post(url, json=requestJson)
    return r.json()

def deletePatient(userEmail, userPassword, patientID):
    global requestJson, r

    userPassword = my_cipher.encrypt(userPassword.encode('utf-8')).decode('utf-8')
    
    requestJson = {'instruction' : 'deletePatient',
            'userEmail'   : userEmail,        
            'userPassword': userPassword,
            'fields' : [patientID]}

    r = requests.post(url, json=requestJson)
    return r.json()

def renamePatient(userEmail, userPassword, newPatientName, patientID):
    global requestJson, r

    userPassword = my_cipher.encrypt(userPassword.encode('utf-8')).decode('utf-8')
    
    requestJson = {'instruction' : 'renamePatient',
            'userEmail'   : userEmail,        
            'userPassword': userPassword,
            'fields' : [patientID, newPatientName]}

    r = requests.post(url, json=requestJson)
    return r.json()

#########

def addMed(userEmail, userPassword, medName, medQty, medQtyUnit, notes,
           time1, time2, time3, patientID):
    global requestJson, r

    userPassword = my_cipher.encrypt(userPassword.encode('utf-8')).decode('utf-8')
    
    requestJson = {'instruction' : 'addMed',
            'userEmail'   : userEmail,        
            'userPassword': userPassword,
            'fields': [medName, medQty, medQtyUnit, notes, time1, time2, time3, patientID]}
    
    r = requests.post(url, json=requestJson)
    return r.json()

def editMed(userEmail, userPassword, medID, medName, medQty, medQtyUnit, notes,
            time1, time2, time3, wasTaken1, wasTaken2, wasTaken3):
    global requestJson, r

    userPassword = my_cipher.encrypt(userPassword.encode('utf-8')).decode('utf-8')
    
    requestJson = {'instruction' : 'editMed',
            'userEmail'   : userEmail,        
            'userPassword': userPassword,
            'fields': [medID, medName, medQty, medQtyUnit, notes, time1, time2, time3, wasTaken1, wasTaken2, wasTaken3]}
    
    r = requests.post(url, json=requestJson)
    return r.json()

def deleteMed(userEmail, userPassword, medID):
    global requestJson, r

    userPassword = my_cipher.encrypt(userPassword.encode('utf-8')).decode('utf-8')
    
    requestJson = {'instruction' : 'deleteMed',
            'userEmail'   : userEmail,        
            'userPassword': userPassword,
            'fields': [medID]}
    
    r = requests.post(url, json=requestJson)
    return r.json()

def tickMedTiming(userEmail, userPassword, medID, timingIndex, state):
    global requestJson, r

    userPassword = my_cipher.encrypt(userPassword.encode('utf-8')).decode('utf-8')
    
    requestJson = {'instruction' : 'tickMedTiming',
            'userEmail'   : userEmail,        
            'userPassword': userPassword,
            'fields': [medID, timingIndex, state]}
    
    r = requests.post(url, json=requestJson)
    return r.json()

def clearTicks(userEmail, userPassword, patientID):
    global requestJson, r

    userPassword = my_cipher.encrypt(userPassword.encode('utf-8')).decode('utf-8')
    
    requestJson = {'instruction' : 'clearTicks',
            'userEmail'   : userEmail,        
            'userPassword': userPassword,
            'fields': [patientID]}
    
    r = requests.post(url, json=requestJson)
    return r.json()
