import mysql.connector as myconn

db = myconn.connect(
    host="localhost",         
    user="root",     
    password="NO", 
    # database="your_database"
)

print(db,"Connection Done.....")