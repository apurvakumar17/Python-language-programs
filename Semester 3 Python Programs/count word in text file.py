with open("mytext.txt", "w") as filew:
    filew.write("Apurva is a good boy studying BCA(H) in MSI")

with open("mytext.txt", "r") as filer:
    content = filer.read()
    new_content = content.split()
    print(len(new_content))
    print("-".join(new_content))
