filename = input("Enter the file name: ")
try:
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()  
        print("Number of words in the file:", len(words))

except FileNotFoundError:
    print("Error: File not found!")
print("\nApurva Kumar, 04814902024")