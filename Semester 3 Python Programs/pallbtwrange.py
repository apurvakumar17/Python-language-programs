start = int(input("Enter start: "))
end = int(input("Enter end: "))

for i in range(start, end + 1):
    if str(i) == str(i)[::-1]:
        print(i, end=" ")