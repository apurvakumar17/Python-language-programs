import csv

with open("practical27_students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Apurva", 20, "BCA"])
    writer.writerow(["Shreyas", 21, "BCA"])
    writer.writerow(["Riya", 19, "BCA"])

print("Data inserted into CSV file successfully!\n")


with open("practical27_students.csv", "r") as file:
    reader = csv.reader(file)

    print("Contents of CSV File:")
    for row in reader:
        print(row)
print("Apurva Kumar, 04814902024")