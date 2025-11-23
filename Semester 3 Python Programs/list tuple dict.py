fruits = ["apple", "banana", "cherry"]
colors = ("red", "green", "blue")
letter = {"A": 1, "B": 2}

fruits.append("A")
fruits.append("A")
fruits.remove("A")
print(fruits)
fruits.insert(5, "C")
fruits.extend(["D", "E", "F", "G"])
print(fruits)
print(fruits.index("A"))
x = fruits.copy()
fruits.clear()

print(colors.count("red"))
print(colors.index("red"))

print(letter.items())
print(letter.keys())
print(letter.values())
letter["C"] = 3
print(letter.popitem())
y = letter.copy()