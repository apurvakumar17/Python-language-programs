import mysql.connector
mydb = mysql.connector.connect(user='root', host='localhost', passwd='1413342', database='soe')
mycursor = mydb.cursor()
mycursor.execute('select * from student')
mydata = mycursor.fetchall()
md = []
for i in mydata:
    i = list(i)
    md.append(i)
print('-:Welcome to Student detail update Screen:-')
print('************************************')
roll = int(input('Enter the student roll no. to search: '))
f = False
for i in md:
    if i[0] == roll:
        print('Data found!')
        print(i)
        f = True
        break
if not f:
    print('Data not found!')
else:
    ans = input('Do you want to update the marks of this student? (y/n) ')
    if ans == 'y':
        m = input('Enter the new marks: ')
        mycursor.execute("update student set marks=" + m + " where Rollno=" + str(roll))
        mydb.commit() 
        print('Student Marks updated successfully!')
        mycursor.execute('select * from student')
        mydata = mycursor.fetchall()
        for i in mydata:
            print(i)






