num=int(input("Enter any number to check: "))
lim=num//2+1
for i in range(1,lim):
    rem=num%i
    if rem==0:
        print("Entered number is a prime")
        break
else:
    print("Entered number is composite")    
