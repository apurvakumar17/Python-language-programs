x="(x+y)/(z*8)"
exp=[]
postfix=""
for i in x:
    if i=="(":
        exp.append(i)
        
    
    elif i in "/*-+":
        exp.append(i)
        
        
    elif i==")":
        x="a"
        while x!="(":
            x=exp.pop()
            if x not in "()":
                postfix+=x
    else:
        postfix+=i

if not len(exp)==0:
    postfix+=exp.pop()
print(postfix)           
        



