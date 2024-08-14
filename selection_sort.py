lst=[8, 7, 13, 1, -9, 4]
for i in range(len(lst)):
    minimum=min(lst[i:len(lst)])
    pstn=lst.index(minimum)
    lst[i],lst[pstn]=lst[pstn],lst[i]
print(lst)    