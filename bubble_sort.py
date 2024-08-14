lst=[8, 7, 13, 1, -9, 4]
for i in range(len(lst)):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            lst[i],lst[i+1]=lst[i+1],lst[i]
            swapped=True
    if not swapped:
        break        
print(lst)            