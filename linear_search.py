x=int(input('Enter number to search: '))
lst=[-9, 1, 4, 7, 8, 13]
for i in range(len(lst)):
    if lst[i]==x:
        print('Number found at index',i)
        break
else:
    print('No element found')
