lst=[]
num=int(input("How many numbers you want in list?: "))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

print("Largest number in the list is :", max(lst), "\nSmallest number in the list is :", min(lst))





