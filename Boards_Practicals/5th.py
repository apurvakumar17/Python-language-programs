import pickle
with open ('studentdata.bin','wb') as fileq:
    record=[['Apurva',1,100],['Himanshu',2,99],['Anubhav',3,98],['Nitin',4,97],
            ['Chandrika',5,96],['Keshav',6,95],['Khushbu',7,94]]
    pickle.dump(record,fileq)
with open('studentdata.bin','rb') as filej:
    f=pickle.load(filej)
    ans='y'
    while ans=='y':
        roll=int(input('Enter the roll no: '))
        upmarks=int(input('Enter the new marks: '))
        f[roll-1][2]=upmarks 
        print('New data: ',f[roll-1])
        with open('studentdata.bin','wb') as filer:
            pickle.dump(f,filer)
        ans=input('Do you want to update more data (y/n) ? ')
    print('Updated data: ')    
with open('studentdata.bin','rb') as filek: 
    fi=pickle.load(filek)
    for k in fi:
        print(k)