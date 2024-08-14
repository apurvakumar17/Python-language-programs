import mysql.connector
mydb=mysql.connector.connect(user='root',host='localhost',passwd='1413342',database='soe')
mycursor=mydb.cursor()
ans='y'
while ans=='y':
        empno=(input('Enter Employe Number: '))
        empname=input('Enter Employee Name: ')
        empgen=input('Enter Employee Gender: ')
        empsal=(input('Enter Employee Salary: '))
        #mycursor.execute("insert into emp values (1,'Apurva','M',200000)")
        mycursor.execute("insert into emp values ("+empno+",'"+empname+"','"+empgen+"',"+empsal+")")
        mydb.commit()
        print('Record stored succrssfully! ')
        ans=input('Do you want to add another employee details ? (y/n): ')
mycursor.execute('select * from emp')
for i in mycursor:
        print(i)

        