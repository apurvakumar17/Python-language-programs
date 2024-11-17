def vopal(x,y):
    vowelcount=0
    x=x.upper()
    if y==1:
        if x==x[::-1]:
            return("Entered string is palindrome")
        else:
            return("Entered string is not a palindrome")
    elif y==2:
        for i in x:
            if i in ["A","E","I","O","U"]:
                vowelcount=vowelcount+1
        return ("There are",vowelcount,"vowels in this string")
    else:
        return ("Invalid choice")
    
a=input("Enter the string: ")
b=int(input("""Enter 1 to check palindrome
               Enter 2 to check number of vowels""")) 
print(vopal(a,b))   