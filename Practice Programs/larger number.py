try:
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    if a>b:
        print(a," is larger number")
    if a<b:
        print(b," is larger number")
    if a==b:
        print("Both are equal")
except:
    print("Invalid Input")
