import random
L=["micro","mouse","debug","cobol","crash"]

micro=list(L[0])
mouse=list(L[1])
debug=list(L[2])
cobol=list(L[3])
crash=list(L[4])

words=[micro,mouse,debug,cobol,crash]
vowel=["a","e","i","o","u"]

for j in words:
    for i in range (0,5):
        if j[i] not in vowel:
            j[i]="_"
    #print(j)

micro1=list(L[0])
mouse1=list(L[1])
debug1=list(L[2])
cobol1=list(L[3])
crash1=list(L[4])

words1=[micro1,mouse1,debug1,cobol1,crash1]

rp=random.randint(0,4)

print(words[rp])
for a in range (0,5):
    c=5-a
    print("You have",c,"chances left")
    g=input("Enter you guess: ")
    print()
    if g not in words1[rp]:
        print("Wrong guess.....")
        print(words[rp])
        print()
    if g in words1[rp]:
        print("Correct guess.....")
        index=words1[rp].index(g)
        words[rp][index]=words1[rp][index]
        print(words[rp])
        print()
        if "_" not in words[rp]:
            print("You won")
            break
        print()
if "_" in words[rp]:
    print("Better luck next time")
