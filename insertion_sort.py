lst=[8, 7, 13, 1, -9, 4]
for i in range(1,len(lst)):
    for j in range(i,0,-1):
        #print(j,end=".")
        if lst[j]<lst[j-1]:
            lst[j],lst[j-1]=lst[j-1],lst[j]
        else:
            continue
    #print()    
print(lst)
