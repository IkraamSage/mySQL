import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="@Lifechoices1234",
    database="lifechoices_online"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE ")

for db in mycursor:
    print(db)
