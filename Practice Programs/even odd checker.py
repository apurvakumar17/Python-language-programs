try:
   a=int(input("Enter integer number to check: "))    #Taking input number
   if a==0:                                     #Checking if input is zero
       print("Zero is neither even nor odd")    
   elif a%2==0:                                 #Checking divisibility by 2
       print(a,"is even")                       
   else:                                        #Printing result
       print(a,"is odd")
except:
    print("Invalid input")
