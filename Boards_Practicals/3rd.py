file1=open("words.txt",'r')
file2=open("nwords.txt",'w')
f=file1.readlines()
file1.close()
new=[]
for i in f:
    if 'a' in i:
        file2.write(i)
    else:
        new.append(i)     
file2.close()        
file3=open("words.txt",'w')
file3.writelines(new)
file3.close()