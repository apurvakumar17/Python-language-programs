#Program to calculate the total marks and his percentage out of 600
print("Program to calculate the total marks and his percentage out of 600")
n=input("Enter the name of Student: ")                                      #Taking input of the name of student
c=input("Enter class and section of the student: ")                         #Taking input of the class of student

m1=int(input("Enter the marks of student in English out of 100: "))         #
m2=int(input("Enter the marks of student in Hindi out of 100: "))           #
m3=int(input("Enter the marks of student in Maths out of 100: "))           #Taking input of marks of each subject
m4=int(input("Enter the marks of student in Science out of 100: "))         #
m5=int(input("Enter the marks of student in Social Science out of 100: "))  #
m6=int(input("Enter the marks of student in Computer Science out of 100: "))#

t=m1+m2+m3+m4+m5+m6                              #Calculated total marks of student

print(n,"got",t,"/600")                          #Printing the total marks out of 600
print("Overall percentage is= ",t/600*100,"%")   #Calculated the overall percentage and printing it

if t>550 :
    print("Very Good",n)









