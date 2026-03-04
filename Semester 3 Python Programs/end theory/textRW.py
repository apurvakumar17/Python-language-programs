with open("myfile.txt","w+") as f:
    f.write("Hello world i am python god of all languages\nI think this line would come in next line what do you say?\n\tA new tab")
    f.seek(0)
    print(f.readline())
    f.seek(0)
    print(f.readlines())
    f.seek(0)
    print(f.read())