file1=open("words.txt")
a=file1.read()
vowel=0
consonents=0
lowercase=0
uppercase=0
for i in a:
    if (i.islower()):
        lowercase+=1
    elif (i.isupper()):
        uppercase+=1
    i=i.lower()
    if (i in ['a','e','i','o','u']):
        vowel+=1
    elif (i not in ['a','e','i','o','u']):
        consonents+=1
print(a)
print("Number of vowels=",vowel)
print("Number of consonents=",consonents)
print("Number of lowercase=",lowercase)
print("Number of uppercase=",uppercase)
file1.close()