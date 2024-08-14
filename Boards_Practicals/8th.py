import csv
with open('datastu.csv','w',newline='') as filej:
    csw=csv.writer(filej,delimiter=',')
    ans='y'
    record=[]
    while ans=='y':
        num=int(input('Enter Employee number: '))
        name=input('Enter Employee name: ')
        salary=int(input('Enter Employee salary: '))
        csw.writerow([num,name,salary])
        ans=input('Do you want to continue (y/n) ?')
    print('Data entered....')
with open('datastu.csv','r',newline='') as fileh:
    imp=int(input('Enter employee number to search: '))
    csr=csv.reader(fileh)
    for i in csr:
        if imp==int(i[0]):
            print('Employee name: ',i[1])
            print('Employee salary: ',i[2])         
            break          

