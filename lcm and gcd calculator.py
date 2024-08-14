#LCM and GCD calculator
print("Enter the values of both numbers which you are required to find LCM and GCF")
choice="y"
while choice=="y":
    x=int(input("Enter number1: "))
    y=int(input("Enter number2: "))

    if x>y:                  #for calculating hcf
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
            
    lcm=x*y//hcf            #for calculating LCM with the help of HCF obtained
    print("LCM of the numbers = ",lcm,"\nHCF of the numbers = ",hcf)#printing the results
    choice=input("Do you find HCF & LCM again? (y/n): ")








    
