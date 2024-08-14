list=[]
n=int(input("How many numbers you want in the list? "))
print("Now, you will be asked to enter the numbers till your desired times")
for i in range (1,n+1):
    x=int(input("Enter the number: "))
    list.append(x)
print("Your original list: ",list)
a=int(input("Enter the number which you want to add to each element of the number: "))    
for i in range(0,len(list)):
    list[i]=list[i]+a
print("Your new list",list)  