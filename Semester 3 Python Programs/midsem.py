print("Apurva\nKumar\tSOE\"Sector-23\"Delhi\'110085\'")
lst = list("Apurva Kumar")
for i in lst:
    print(i, end='.')
print('\n')

print(id(lst))
lst.append(" ")
print(id(lst))

print(len(lst))
lst.extend(list("Tushar Nath"))

lst.insert(7, "c")
print(lst[0:7] + lst[7:85])
print(id(lst))
# lst.sort(reverse = True)

#SET

set1 = set(lst)
set1.remove("a")
set1.discard("1")
set1.add("z")
set2 = set1.copy()
set2.clear()
print(set2)
print(set1)
for i in lst:
    print(i, end='')
print("\n")

di = {"17h":"Hotesh", "20s":"Shreyas", "48a":"Apurva"}
print(di["17h"])

di["kkk"] = "kumars"

del di["kkk"]

for i in di.keys():
    print(f"{i}:{di[i]}")
print(di.items())

text = "Hello, World!" 
print(text[::2])

t1 = tuple("Apurva")
print(t1)
