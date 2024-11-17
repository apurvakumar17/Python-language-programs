nterms=int(input("How many terms you want? "))
n1=0
n2=1
count=0

if nterms<=0:
   print("Please enter a positive integer")

elif nterms==1:
   print("Fibonacci sequence upto",nterms,"=",n1)

else:
   print("Fibonacci series:")
   while count<nterms:
       print(n1)
       nth=n1+n2
       n1=n2
       n2=nth
       count+=1
















       
