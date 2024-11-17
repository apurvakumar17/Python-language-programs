print(" Program to input a list of elements and search for a given element in the list")
list=[]
num=int(input("How many numbers in the list: "))
for n in range(num):
    numbers=int(input("Enter number: "))
    list.append(numbers)
print("The entered list is ",list)
length=len(list)
element=int(input("Enter the element which you want to search for: "))
for i in range(0,length):
    if element==list[i]:
        print("Element",element,"found at index",i)
        break
else:
    print(element," is not found!")












    





    
