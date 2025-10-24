def is_heterogram(s):
    s = s.lower()
    return len(set(s)) == len(s)

print("\"Lamp\" is Heterogram: ", is_heterogram("lamp"))
print("\"Letter\" is Heterogram: ", is_heterogram("letter"))

print("\nApurva Kumar, 04814902024")