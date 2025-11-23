import csv

with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow([1, "Apurva", "Kumar"])
    writer.writerow([1, "Apurva", "Kumar"])
    writer.writerow([1, "Apurva", "Kumar"])
    writer.writerow([1, "Apurva", "Kumar"])
    writer.writerow([1, "Apurva", "Kumar"])

with open("students.csv","r", newline='') as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)