import mysql.connector

dataBase = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd =''
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE waste_management")

print("Database Created!!")