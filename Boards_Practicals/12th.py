import csv
ids=[]
p=[]
with open ('base.csv','r') as filed:
    f=csv.reader(filed)
    for i in f:
        ids.append(i[0])
        p.append(i[1])
        #print(i)

uid=input('Enter your username: ')
if uid in ids:
    for i in range(0,len(ids)):
        if ids[i]==uid:
            id=i
            break
    while True:
        password=input('Enter your password: ')
        if password==p[id]:
            print('Password verified! ')
            idc=input('Enter the username to search: ')
            if idc in ids:
                for i in range(0,len(ids)):
                    if ids[i]==idc:
                        ij=i
                        break
                print('Password for this username is: ',p[ij])    
            else:
                print('Entered username not found! ')         
            break
        else:
            print('Invalid password! ')  
else:
    print('Invalid username!')



