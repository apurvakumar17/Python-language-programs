print('''1. Addition
2. Subtraction
3. Multiplication
4. Division''')
num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number : '))
ch=int(input('Enter your choice (1/2/3/4) ?'))
if ch==1:
    print('The addition of two number is: ',num1+num2)
elif ch==2:
    print('The subtraction of two number is: ',num1-num2)
elif ch==3:
    print('The multiplication of two number is: ',num1*num2)
elif ch==4:
    if num2!=0:
        print('The division of two number is: ',num1/num2)
    else:    
        print('Divisor can not be zero!')
else:
    print('Invalid choice!!')



