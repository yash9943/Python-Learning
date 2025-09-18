import mysql.connector as connector

# Reconnect to the newly created database
conn = connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    database='first'
)

print("Create Succesfully..")