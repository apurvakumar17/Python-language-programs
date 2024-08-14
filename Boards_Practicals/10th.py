def fact(num):
    f=1
    for i in range (1,num+1):
        f=f*i
    return(f)
def sum(num):
    f=0
    for i in range (0,num+1):
        f=f+i
    return(f)
number=int(input('Enter the number: '))    
print('''1.Factorial of entered number
2.Sum of all digits up to entered number ''')
ch=int(input('Enter your choice (1/2): '))
if ch==1:
    print('Factorial of entered number is: ',fact(number))
elif ch==2:
    print('Sum of all digits up to entered number is: ',sum(number))
else:
    print('Invalid choice!!')


