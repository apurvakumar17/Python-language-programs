source_file = "practical25_source.txt"
destination_file = "practical25_destination.txt"

with open(source_file, 'r') as src:
    content = src.read() 

with open(destination_file, 'w') as dest:
    dest.write(content) 

print("File copied successfully!")
print("\nApurva Kumar,04814902024")