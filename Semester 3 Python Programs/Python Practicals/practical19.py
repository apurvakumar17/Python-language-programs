print("=== LIST EXAMPLE ===")
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)
fruits.append("mango")
print("After appending 'mango':", fruits)
fruits.remove("banana")
print("After removing 'banana':", fruits)
print("Second element:", fruits[1],"\n")

print("=== TUPLE EXAMPLE ===")
colors = ("red", "green", "blue")
print("Tuple:", colors)
print("First element:", colors[0])
print("Length of tuple:", len(colors),"\n")

print("=== DICTIONARY EXAMPLE ===")
letter = {"A": 1, "B": 2}
print("Dictionary:", letter)
print("Access value by key (A):", letter["A"])
letter["C"] = 3
print("After adding new pair:", letter)
letter.pop("B")
print("After removing 'B':", letter)

print("\nApurva Kumar," \
" 04814902024")