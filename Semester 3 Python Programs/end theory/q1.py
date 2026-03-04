with open("greetings.txt","w") as fp:
    l1 = input("Line1: ") + "\n"
    l2 = input("Line1: ") + "\n"
    l3 = input("Line3: ") + "\n"
    msg = [l1,l2,l3]
    fp.writelines(msg)
with open("greetings.txt","a") as fp:
    l4 = input("Line4: ")
    fp.write(l4)