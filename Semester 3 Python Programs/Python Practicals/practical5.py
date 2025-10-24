def are_disjoint(set1, set2):
    for elem1 in set1:
        for elem2 in set2:
            if elem1 == elem2:
                return False 
    return True

setA = {1, 2, 3}
setB = {4, 5, 6}
setC = {3, 7, 8}

print("setA: ", setA)
print("setB: ", setB)
print("setC: ", setC)

print(are_disjoint(setA, setB))
print(are_disjoint(setA, setC))

print("\nApurva Kumar, 04814902024")