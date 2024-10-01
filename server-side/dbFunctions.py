# File: dbFunctions.py
import os
import mysql.connector as conn
import hashlib
from cryptography.fernet import Fernet

key = bytes(open('credentials.txt', 'r').read(), 'utf-8')
my_cipher = Fernet(key)
pwd = ''

def connectDB():
    global db, cursor
    
    db = conn.connect(host='localhost', port=3306, user='root',
                      database='mednotedatabase', autocommit=True)
    
##    db = conn.connect(host='Vikhyat.mysql.pythonanywhere-services.com',
##                        database='Vikhyat$mednotedatabase', user='Vikhyat',
##                        passwd=pwd, autocommit=True)
    
    cursor = db.cursor()

def executeSql(sql, args, commit=False, returnResult=True):
    try:
        # Execute sql command with the provided arguments
        cursor.execute(sql, args)

    except (conn.errors.DatabaseError) as e:
        # Print error statement to be seen in server log
        print('Found DatabaseError when executing:\n', str(e), '\n', sql)

        # Try to re-connect to database and execute command again
        connectDB()
        cursor.execute(sql, args)

    # Commit changes to the database if requested
    if commit:
        db.commit()

    # Return SQL command results if requested
    if returnResult:
        result = cursor.fetchall()
        return result

def auth(userEmail, userPassword):

    # Decrypt password received from client
    userPassword = my_cipher.decrypt(userPassword.encode('utf-8'))

    # Fetch the hashed key stored in the database for this user
    sql = 'SELECT userKey FROM users WHERE userEmail=%s'
    sqlResult = executeSql(sql, (userEmail, ))

    # Return error if userEmail not found
    if sqlResult == []:
        return (False, 'Email not found!')

    # User's hashed key in database
    dbKey = sqlResult[0][0]

    # Fetch the salt stored in the database for this user
    sql = 'SELECT salt FROM users WHERE userEmail=%s'
    sqlResult = executeSql(sql, (userEmail, ))

    # User's salt in database
    salt = sqlResult[0][0]

    # Combine the password plaintext & salt and encrypt them using 100000 iterations of a hash function
    key = hashlib.pbkdf2_hmac('sha256', userPassword, salt.encode('utf-8'), 100000, dklen=50).hex()

    # Approve authentication if the key derived from the entered password matches the database key
    if dbKey == key:
        return (True, '')

    # Return authentication error if keys do not match
    return (False, 'Incorrect password!')

def registerUser(userEmail, userPassword):

    # Decrypt password received from client
    userPassword = my_cipher.decrypt(userPassword.encode('utf-8'))

    # Generate a random 32-byte string to use as salt and convert it to hexadecimal format
    salt = os.urandom(32).hex()

    # Combine the password plaintext & salt, and encrypt them using 100000 iterations of a hash function
    key = hashlib.pbkdf2_hmac('sha256', userPassword, salt.encode('utf-8'), 100000, dklen=50).hex()

    # Insert user email, hashed key, and salt into database
    sql = 'INSERT INTO `users`(`userEmail`, `userKey`, `salt`) VALUES (%s,%s,%s)'
    executeSql(sql, (userEmail, key, salt, ), True, False)

def fetchData(userEmail):
    sql = 'SELECT userID FROM users WHERE userEmail=%s'
    userID = executeSql(sql, (userEmail, ))[0][0]

    sql = 'SELECT * FROM patients WHERE (patients.userID = %s)'
    patients = executeSql(sql, (userID, ))
    patients = [(p[0], p[1]) for p in patients]

    sql = '''SELECT
medID, medName, qty, qtyUnit, notes, DATE_FORMAT(medTime1, "%H:%i"),
DATE_FORMAT(medTime2, "%H:%i"), DATE_FORMAT(medTime3, "%H:%i"), wasTaken1, wasTaken2,
wasTaken3, patientID
            FROM meds WHERE
(SELECT patients.userID from patients WHERE patients.patientID = meds.patientID) = %s'''
    meds = executeSql(sql, (userID, ))

    return (True, (patients, meds))

def addPatient(userEmail, patientName):

    # Fetch userID
    sql = 'SELECT userID FROM users WHERE userEmail=%s'
    userID = executeSql(sql, (userEmail, ))[0][0]

    # Count number of patients under user
    sql = 'SELECT SUM(CASE WHEN userID=%s THEN 1 ELSE 0 END) FROM patients'
    numPatients = executeSql(sql, (userID, ))[0][0]

    # Interpret SQL's NULL value as 0
    if numPatients is None:
        numPatients = 0

    # Check if maximum patient count has been reached
    if numPatients >= 20:
        # Return status 'False' with error code
        return (False, 'You cannot have more than 20 patients in the same account!')

    # Fetch patient names under user
    sql = 'SELECT patientName FROM patients WHERE userID=%s'
    patientNames = [tup[0] for tup in executeSql(sql, (userID, ))]

    # Check if new patient name already exists under user
    if patientName in patientNames:
        # Return status 'False' with error code
        return (False, 'You already have another patient with this name!')

    # Add patient to database
    sql = 'INSERT INTO `patients`(`patientName`, `userID`) VALUES (%s, %s)'
    executeSql(sql, (patientName, userID, ), True, False)

    # Fetch new patientID
    sql = 'SELECT patientID FROM patients WHERE (userID=%s AND patientName=%s)'
    patientID = executeSql(sql, (userID, patientName, ))[0][0]

    # Return status 'True' with patientID
    return (True, patientID)

def renamePatient(userEmail, patientID, newPatientName):

    # Ensure patient exists under user
    sql = 'SELECT userID FROM users WHERE userEmail=%s'
    userID = executeSql(sql, (userEmail, ))[0][0]

    sql = 'SELECT userID FROM patients WHERE patientID=%s'
    patientUserID = executeSql(sql, (patientID, ))[0][0]

    if userID != patientUserID:
        return (False, 'Access error: this patient is not listed under your account!')

    # Ensure patient (name) doesn't already exist
    sql = 'SELECT patientName FROM patients WHERE userID=%s'
    patientNames = [tup[0] for tup in executeSql(sql, (userID, ))]

    if newPatientName in patientNames:
        return (False, 'You already have another patient with this name!')

    # Rename patient
    sql = 'UPDATE patients SET patientName=%s WHERE patientID=%s'
    executeSql(sql, (newPatientName, patientID, ), True, False)

    return (True, '')

def deletePatient(userEmail, patientID):

    # Fetch userID
    sql = 'SELECT userID FROM users WHERE userEmail=%s'
    userID = executeSql(sql, (userEmail, ))[0][0]

    # Fetch userID for the user who patientID is registered under
    sql = 'SELECT userID FROM patients WHERE patientID=%s'
    patientUserID = executeSql(sql, (patientID, ))[0][0]

    # Check if the patient is not under the user making the delete request
    if userID != patientUserID:
        # Return status 'False' with error code
        return (False, 'Access error: this patient is not listed under your account!')

    # Delete patient from database
    sql = 'DELETE FROM patients WHERE patientID=%s'
    executeSql(sql, (patientID, ), True, False)

    # Return status 'True' with no other data
    return (True, '')

######################################

def addMed(userEmail, medName, medQty, medQtyUnit, notes, time1, time2, time3, patientID):
    # Ensure patient exists under user
    sql = 'SELECT userID FROM users WHERE userEmail=%s'
    userID = executeSql(sql, (userEmail, ))[0][0]

    sql = 'SELECT userID FROM patients WHERE patientID=%s'
    patientUserID = executeSql(sql, (patientID, ))[0][0]

    if userID != patientUserID:
        return (False, 'Access error: this patient is not listed under your account!')

    # Ensure maximum medicine count isn't surpassed
    sql = 'SELECT SUM(CASE WHEN patientID=%s THEN 1 ELSE 0 END) FROM meds'
    numMeds = executeSql(sql, (patientID, ))[0][0]

    # Interpet SQL's NULL value as 0
    if numMeds is None:
        numMeds = 0

    if numMeds >= 50:
        return (False, 'You cannot have more than 50 medicines for the same patient!')

    # Ensure medicine (name) doesn't already exist
    sql = 'SELECT SUM(CASE WHEN (patientID=%s AND medName=%s) THEN 1 ELSE 0 END) FROM meds'
    numMeds = executeSql(sql, (patientID, medName, ))[0][0]

    # Interpet SQL's NULL value as 0
    if numMeds is None:
        numMeds = 0

    if numMeds>0:
        return (False, 'You already have another medicine with this name!')

    # Add medicine to database
    args = [medName, medQty, medQtyUnit, notes, time1, time2, time3, patientID]

    sql = '''INSERT INTO `meds`(`medName`, `qty`, `qtyUnit`, `notes`,
`medTime1`, `medTime2`, `medTime3`, `patientID`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    executeSql(sql, args, True, False)

    sql = 'SELECT medID FROM meds WHERE (patientID=%s AND medName=%s)'
    medID = executeSql(sql, (patientID, medName, ))[0][0]

    return (True, medID)

def editMed(userEmail, medID, medName, medQty, medQtyUnit, notes, time1, time2, time3, wasTaken1, wasTaken2, wasTaken3):

    # Ensure medicine exists under user
    sql = 'SELECT userID FROM users WHERE userEmail=%s'
    userID = executeSql(sql, (userEmail, ))[0][0]

    sql = 'SELECT patientID FROM meds WHERE medID=%s'
    patientID = executeSql(sql, (medID, ))[0][0]

    sql = 'SELECT userID FROM patients WHERE patientID=%s'
    patientUserID = executeSql(sql, (patientID, ))[0][0]

    if userID != patientUserID:
        return (False, 'Access error: this medicine is not listed under your account!')

    # Ensure medicine (name) doesn't already exist with another med ID
    
    sql = 'SELECT medID FROM meds WHERE (patientID=%s AND medName=%s)'
    sameNameMedID = executeSql(sql, (patientID, medName, ))

    if sameNameMedID != []:
        sameNameMedID = sameNameMedID[0][0]

        if sameNameMedID != medID:
            return (False, 'You already have another medicine with this name!')
        
    # Edit medicine
    args = [medName, medQty, medQtyUnit, notes, time1, time2, time3, wasTaken1, wasTaken2, wasTaken3, medID]

    sql = '''UPDATE meds
    SET medName=%s, qty=%s, qtyUnit=%s, notes=%s, medTime1=%s, medTime2=%s, medTime3=%s, wasTaken1=%s, wasTaken2=%s, wasTaken3=%s
    WHERE medID=%s'''

    executeSql(sql, args, True, False)

    return (True, '')

def deleteMed(userEmail, medID):

    # Ensure medicine exists under user
    sql = 'SELECT userID FROM users WHERE userEmail=%s'
    userID = executeSql(sql, (userEmail, ))[0][0]

    sql = 'SELECT patientID FROM meds WHERE medID=%s'
    patientID = executeSql(sql, (medID, ))[0][0]

    sql = 'SELECT userID FROM patients WHERE patientID=%s'
    patientUserID = executeSql(sql, (patientID, ))[0][0]

    if userID != patientUserID:
        return (False, 'Access error: this medicine is not listed under your account!')

    # Delete medicine
    sql = 'DELETE FROM meds WHERE medID=%s'
    executeSql(sql, (medID, ), True, False)

    return (True, '')

def tickMedTiming(userEmail, medID, medTimingIndex, state):

    # Ensure medicine exists under user
    sql = 'SELECT userID FROM users WHERE userEmail=%s'
    userID = executeSql(sql, (userEmail, ))[0][0]

    sql = 'SELECT patientID FROM meds WHERE medID=%s'
    patientID = executeSql(sql, (medID, ))[0][0]

    sql = 'SELECT userID FROM patients WHERE patientID=%s'
    patientUserID = executeSql(sql, (patientID, ))[0][0]

    if userID != patientUserID:
        return (False, 'Access error: this medicine is not listed under your account!')

    # Tick medicine timing
    sql = "UPDATE meds SET wasTaken" + str(medTimingIndex+1) + "=%s WHERE medID=%s"
    executeSql(sql, (state, medID, ), True, False)

    return (True, '')

def clearTicks(userEmail, patientID):

    # Ensure patient exists under user
    sql = 'SELECT userID FROM users WHERE userEmail=%s'
    userID = executeSql(sql, (userEmail, ))[0][0]

    sql = 'SELECT userID FROM patients WHERE patientID=%s'
    patientUserID = executeSql(sql, (patientID, ))[0][0]

    if userID != patientUserID:
        return (False, 'Access error: this patient is not listed under your account!')

    # Rename patient
    sql = 'UPDATE meds SET wasTaken1=0, wasTaken2=0, wasTaken3=0 WHERE patientID=%s'
    executeSql(sql, (patientID, ), True, False)

    return (True, '')
