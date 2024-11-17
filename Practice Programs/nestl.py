if __name__ == '__main__':
    stuclass=[]
    printl=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stuclass.append([name,score])
        
    l=len(stuclass)
    min1=99999999999999
    min2=99999999999999
    for i in range(0,l):
        if (stuclass[i][1]<min1):
            min1=stuclass[i][1]
            
    for j in range(0,l):
        if (stuclass[j][1]>min1 and stuclass[j][1]<min2):
            min2=stuclass[j][1]
            
    for k in range(0,l):
        if (min1==stuclass[k][1]):
            printl.append(stuclass[k][0])
            
    for m in range(0,l):
        if (min2==stuclass[m][1]):
            printl.append(stuclass[m][0])  
            
    printl.sort()
    for n in printl:
        print(n)
            