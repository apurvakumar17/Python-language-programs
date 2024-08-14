import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='1413342',database='soe')
mycursor=mydb.cursor()
mycursor.execute ('select * from student')
mydata=mycursor.fetchall()
md=[]
for i in mydata:
    i=list(i)
    md.append(i)
print('-:Welcome to Student Search Screen:-')  
print('************************************')  
roll=int(input('Enter the student roll no. to search: '))
f=False
for i in md:
    if i[0]==int(roll):
        print('Data found! ')
        print(i)
        f=True
        break
if not f:
    print('Data not found! ')



    

