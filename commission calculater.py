try:
    s=int(input("Enter your monthly sale: "))
    c=0
    if s<=0:
        print("This can't be right info")
    elif s<500000:
        c=(s*5)/100
        print("Your commission is Rs.",c)
    else:
        c=(s*10)/100
        print("Your commission is Rs.",c)
except:
    print("an error occured")
    
    
    
