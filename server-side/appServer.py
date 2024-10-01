# File: appServer.py
from flask import Flask, request
import dbFunctions

dbFunctions.connectDB()

app = Flask(__name__)

@app.route('/', methods=['POST'])
def result():
    # Fetch data in client request JSON
    req = request.json

    # Read instruction and credentials from client request
    instruction = req['instruction']
    userEmail, userPassword = req['userEmail'], req['userPassword']

    # Check client credentials through database
    authSuccess, authResult = dbFunctions.auth(userEmail, userPassword)

    # Check if client instruction is to create a new user
    if instruction == 'registerUser':
        # Return 'email exists eror' if the email is not missing in the database
        if authResult != 'Email not found!':
            return {'status':False, 'result': 'Email already exists!'}

        # Register new user and return status 'True' with no data
        dbFunctions.registerUser(userEmail, userPassword)
        return {'status':True, 'result':''}

    # Return error if credentials were not correct
    if not authSuccess:
        return {'status':False, 'result':authResult}

    # Return True if client instruction is just to log in to account
    if instruction == 'loginUser':
        return {'status':True, 'result':''}

    # Define all the valid instructions that exist as dbFunctions functions
    validInstructions = ['fetchData', 'addPatient', 'renamePatient', 'deletePatient',
                         'addMed', 'editMed', 'deleteMed', 'tickMedTiming', 'clearTicks']

    # Check if client instructions is a valid instruction
    if instruction in validInstructions:
        # Fetch the function corresponding to the client instruction
        func = eval('dbFunctions.'+instruction)

        # Call the relevant function and return its value to the client
        success, result = func(userEmail, *req['fields'])
        return {'status':success, 'result':result} 

    # Return an 'Invalid Instruction' error if nothing has returned a response yet
    return {'status':False, 'result': "Invalid instruction"}

if __name__ == '__main__':
    app.run()
