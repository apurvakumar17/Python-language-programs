try:
    ba=int(input("Enter your total bill amount: "))
    pm=input("Enter your payment mode in small letters: ")
    dis=ba
    if pm=="credit card":
        dis=ba-(ba*10)/100
        print("10% discount given to you")
        print("Net payable amount:Rs.",dis)
    elif pm=="debit card":
        dis=ba-(ba*5)/100
        print("5% discount given to you")
        print("Net payable amount:Rs.",dis)
    elif pm=="net banking":
        dis=ba-(ba*2)/100
        print("2% discount given to you")
        print("Net payable amount:Rs.",dis)
    else:
        print("No discount given to you")
        print("Net payable amount:Rs.",dis)
except:
    print("An error occured")
