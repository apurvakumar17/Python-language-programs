list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

print("Set 1: ", set1)
print("Set 2: ", set2)

diff1 = set1.difference(set2)
print("Items in list1 but not in list2:", diff1)

diff2 = set2.difference(set1)
print("Items in list2 but not in list1:", diff2)

sym_diff = set1.symmetric_difference(set2)
print("Items in either list but not both:", sym_diff)

print("\nApurva Kumar, 04814902024")