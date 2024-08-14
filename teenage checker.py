try:
    age=int(input("Enter your age: "))
    if age<0:
        print("Invalid age!")
    elif age<15:
        print("You are not a teenager")
    elif age<=17:
        print("You are a teenager")
    else:
        print("You are not a teenager")
except:
    print("Invalid input")
