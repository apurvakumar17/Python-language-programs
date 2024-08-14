print('''Stack Operations
****************
1. Push
2. Pop
3. Peek
4. Display''')
stack=[]
ans='y'
while ans=='y':
    ch=int(input('Enter your choice (1/2/3/4): '))
    if ch==1:
        elem=input('Enter the element to push: ')
        stack.append(elem)
    elif ch==2:
        if stack==[]:
            print('Cannot pop from empty stack')
        else:    
            print('Deleted element is: ',stack.pop())
    elif ch==3:
        print('Top most element of stack is: ',stack[-1])
    elif ch==4:
        print('Stack elements are: ')
        for i in stack:
            print(i)
    else:
        print('Ivalid choice!!')
    ans=input('Do you want to perform another stack operation(y/n)? ')



        
