import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='1413342',database='soe')
mycursor=mydb.cursor()
mycursor.execute('select * from student')
mydata=mycursor.fetchmany(3)
for i in mydata:
    print(i)    
nrow=mycursor.rowcount
print(nrow,'records found!')








'''import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='1413342',database='soe')
mycursor=mydb.cursor()
mycursor.execute('select * from student')
mydata=mycursor.fetchone()
print(mydata) 
nrow=mycursor.rowcount
print(nrow,'records found!')
print('#####################')
mydata=mycursor.fetchone()
print(mydata) 
nrow=mycursor.rowcount
print(nrow,'records found!')'''


'''import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='1413342',database='soe')
mycursor=mydb.cursor()
mycursor.execute('select * from student')
mydata=mycursor.fetchall()
for i in mydata:
    print(i)    
nrow=mycursor.rowcount
print(nrow,'records found!')'''
