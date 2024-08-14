import pickle
with open ('student.bin','wb') as fileh:
    record=[['Apurva',1],['Himanshu',2],['Anubhav',3],['Nitin',4],
            ['Chandrika',5],['Keshav',6],['Khushbu',7]]
    pickle.dump(record,fileh)
with open ('student.bin','rb') as filej:
    f=pickle.load(filej)
    roll=int(input("Enter the roll no.: "))
    for i in f:
        if i[1]==roll:
            print('Student name is: ',i[0])
            break
    l=[]    
    for i in f:
        l.append(i[1])
    if roll not in l:
        print('Student name with that roll no. not found!')     