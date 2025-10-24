n = int(input("Enter the number of terms: "))
a, b = 0, 1

print(f"Fibonacci Series upto {n}:")
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c

print("\nApurva Kumar, 04814902024")