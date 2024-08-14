import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", passwd="1413342")
if con.is_connected():
    print('Succesfully connected!! ')


