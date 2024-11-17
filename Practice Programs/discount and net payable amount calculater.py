try:
    ba=int(input("Enter your total bill amount: "))
    dis=ba
    if ba>=20000:
        dis=ba-(ba*15)/100
        print("15% discount given to you")
        print("Net payable amount:Rs.",dis)
    elif ba>=15000:
        dis=ba-(ba*10)/100
        print("10% discount given to you")
        print("Net payable amount:Rs.",dis)
    elif ba>=10000:
        dis=ba-(ba*5)/100
        print("5% discount given to you")
        print("Net payable amount:Rs.",dis)
    else:
        print("No discount given to you")
        print("Net payable amount:Rs.",dis)
except:
    print("Invalid input")
    
