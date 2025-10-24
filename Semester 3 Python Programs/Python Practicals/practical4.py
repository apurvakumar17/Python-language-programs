from itertools import combinations

my_set = {1, 2, 3, 4}
k = 2

print("Set: ", my_set)
print()
for subset in combinations(my_set, k):
    print(subset)

print("\nApurva Kumar, 04814902024")