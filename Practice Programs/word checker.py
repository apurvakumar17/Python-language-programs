line=input("Enter the statement: ")
word=input("Enter the word to check in statement: ")
if word in line:
    print("'",word,"' is present in '",line,"' statement")
else:
    print("'",word,"' is not present in '",line,"' statement")
    
