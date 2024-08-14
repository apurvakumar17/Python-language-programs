lst = [29, 11, 74, 67, 38, 13]
hasht=[]
ind={}

for i in lst:
    ind[i%10]=i
print(ind)

for i in range(max(ind)+1):
    hasht.append(None)
print(hasht)           #[None, None, None, None, None, None, None, None, None, None]

for i in ind:
    hasht[i]=ind[i]
print(hasht)        #[None, 11, None, 13, 74, None, None, 67, 38, 29]

num=int(input("Enter the number to search: "))
if hasht[num%10]:
    print("Number found at index",num%10)
else:
    print("Number not found")