string=input("Enter the word to check: ")  #Taking string input
string=string.upper()             #Converting whole string to Upper case
vowel=0                           #Defining values
consonant=0                       
vow=""                            
cons=""                           
for i in range(0,len(string)):                  #Loop for checking vowels & consonant
    if string[i] in ["A","E","I","O","U"]:      
        vowel=vowel+1                           #Counting number of vowels in the string
        vow=vow+string[i]                       #Registring all the vowels in one variable
    if string[i] not in ["A","E","I","O","U"]:
        consonant=consonant+1                   #Counting number of consonant in the string
        cons=cons+string[i]                     #Registring all the consonants in one variable
print("There are total",len(string),"letters in this word")  #Printing no. of letters in string
print("There are",vowel,"vowels")                            #Printing no. of vowels
print("There are",consonant,"consonants")                    #Printing no. of consonant
print("Vowels in this word: ",vow.lower())                   #Printing all the vowels in lower case
print("Consonants in this word: ",cons.lower())              #Printing all the consonant in lower case




