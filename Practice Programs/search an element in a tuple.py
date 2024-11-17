print(" Program to input a tuple of elements and search for a given element in the tuple")
tuple=eval(input("Enter the tuple elements: "))
print("The entered tuple is ",tuple)
length=len(tuple)
element=input("Enter the element which you want to search for: ")
for i in range(0,length):
    if element==tuple[i]:
        print("Element",element,"found at index",i)
        break
else:
    print(element,"is not found!")












    
