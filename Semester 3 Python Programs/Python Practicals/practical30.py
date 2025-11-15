def find_duplicates(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    duplicates = set1.intersection(set2)
    return list(duplicates)

list1 = [1, 2, 3, 4, 5, 3, 2]
list2 = [4, 5, 6, 7, 5, 8]

result = find_duplicates(list1, list2)

print(list1)
print(list2)
print("Duplicate elements in both lists:", result)
print("\nApurva Kumar, 04814902024")