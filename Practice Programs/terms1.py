x=int(input("Enter value of x :")) 
n=int(input("Enter value of n :")) 
terms=[] 
factorials=[] 
fact=1 
for i in range(1,n+1): 
    fact=fact*i 
    factorials.append(fact) 
print(factorials) 
for i in range(1,n+1): 
    terms.append((x**i)/factorials[i-1]) 
print(terms) 
 
value=0 
for i in range(0,n): 
    if i%2==0: 
        value+=terms[i] 
    elif i%2!=0: 
        value-=terms[i] 
print(value)