print("Welcome to calculator")

a=float(input("Enter the first number"))
b=float(input("Enter the second number"))
print("What you want to do?\n\t\t1.Add\n\t\t2.Subtract\n\t\t3.Multiply\n\t\t4.Divide\n\t\t5.Exit")
choice=int(input("Enter(1/2/3/4) from above: "))
if choice==1:
    print("Sum=",a+b)
elif choice==2:
    print("Difference=",a-b)
elif choice==3:
    print("Product=",a*b)
elif choice==4:
    print("Product=",a/b)
elif choice==5:
    print("OK!")
else:
    print("Invalid choice")
