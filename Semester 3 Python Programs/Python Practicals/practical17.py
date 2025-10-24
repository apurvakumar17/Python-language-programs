def Pall_n(start, end):
    print(f"\nPalindrome numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if str(num) == str(num)[::-1]:
            print(num, end=" ")
    print()

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

Pall_n(start, end)
print("\nApurva Kumar, 04814902024")