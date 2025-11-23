n = int(input("Enter: "))
n1 = 0
n2 = 1

if n < 1:
    print("Please enter greater 0")
elif n==1:
    print(n1)
elif n==2:
    print(f"{n1} {n2}")
else:
    print(f"{n1} {n2}", end=" ")
    for i in range(n):
        temp = n1 + n2
        print(temp, end=" ")
        n1 = n2
        n2 = temp
