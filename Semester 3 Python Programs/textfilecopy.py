content=""
with open("mytext.txt","r") as file:
    content = file.read()

print(content)
with open("mytext_copy.txt", "w") as filew:
    filew.write(content)