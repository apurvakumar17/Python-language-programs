file1=open("words.txt")
a=file1.readlines()
for i in a:
    d=list(i)
    for j in d:
        if j!=' ':
            print(j,end='')
        else:
            print('#',end='')
file1.close()