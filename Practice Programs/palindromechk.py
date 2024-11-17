name=input("Enter your name: ")
revn=""
for i in name:
    revn=i+revn 
print("Reversed string : ", revn) 
 
if(name==revn): 
    print("Your name is palindrome!") 
else:
    print("Your name is not palindrome")
    
