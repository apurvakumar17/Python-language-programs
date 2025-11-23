list1 = [1, 2, 3, 4, 5, 3, 2]
list2 = [4, 5, 6, 7, 5, 8]
list3 = [1, 2, 6, 5, 7]
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

print(set1.intersection(set2)) #duplicates of both lists
print(set1.issuperset(set2)) 

for i in range(len(list1)):
    list1[i] = list1[i] ** 2
print(list1)

print(set1 & set2 & set3)
print("".join({"a","b","c"}))
print(str({"a","b","c"}))

set1.difference_update({1, 2})
print(set1)

set1.add(27)
set1.update([1, 2])
print(set1)

set3 = {7, 8, 9}
set4 = {10, 11, 12,9}
flg = True
for i in set3:
    for j in set4:
        if i == j:
            flg = False
            print("Is not disjoint")
            break

if (flg):
    print("Is Disjoint")

from itertools import combinations

k= 2
for i in combinations(set4, k):
    print(i)

str1 = "apurva"
str2 = "Home"

if len(str1) == len(set(str1)):
    print("it is heterogram")
    print(set(str1))

print(set1.symmetric_difference(set2))