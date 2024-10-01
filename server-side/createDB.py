# File: createDB.py

import mysql.connector as conn

pwd = ''
    
db = conn.connect(host='localhost', port=3306, user='root', autocommit=True)
# db = conn.connect(host='Vikhyat.mysql.pythonanywhere-services.com', user='Vikhyat', passwd=pwd, autocommit=True)

cursor = db.cursor()

def executeScriptsFromFile(filename):
    file = open(filename, 'r', encoding='utf-8')
    sqlScript = file.read()
    file.close()

    sqlCommands = sqlScript.split(';')

    for command in sqlCommands:
        try:
            cursor.execute(command)
        except Exception as e:
            print("Command skipped: ", str(e))

executeScriptsFromFile('creationScript.sql')
executeScriptsFromFile('addData.sql')

