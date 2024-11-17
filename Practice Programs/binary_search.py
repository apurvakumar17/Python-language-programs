lst=[-9, 1, 4, 7, 8, 13] 
x=int(input('Enter number to search: ')) #x=7
found=False
left=0             #left=0,3,3
right=len(lst)-1   #right=5,5,3
while left<=right:  # true,true
    mid=(left+right)//2    #mid=2,mid=4,mid=3
    if lst[mid]==x:         #false,false,true
        print('Found at index:',mid)      #-,-,print found
        found=True
        break
    elif lst[mid]<x:         #true,false
        left=mid+1           #left=3
    else: 
        right=mid-1          #-,right=3
if not found:
    print('Not Found')
       
        