import pickle
with open('studata.bin','wb') as fileh:
    ans='y'
    record=[]
    while ans=='y':
        roll=int(input('Enter roll number: '))
        name=input('Enter name: ')
        record.append([roll,name])
        ans=input('Do you want to add another student detail? (y/n): ')
    pickle.dump(record,fileh)
with open('studata.bin','rb') as filej:
    f=pickle.load(filej)
    l=[]
    for i in f:
        l.append(i[0])
    check=int(input('Enter roll no. of student to search: '))
    if check in l:
        for i in f:
            if i[0]==check:
                print(i)
                break
    else:
        print('Student with that roll number not found! ')    
        
