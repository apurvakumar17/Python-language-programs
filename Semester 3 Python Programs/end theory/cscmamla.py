import csv

with open("students.csv", "r", newline="") as f:
    # writer = csv.writer(f)

    # while True:
    #     name = input("Enter name of student: ")
    #     class1 = int(input("Enter Class: "))
    #     marks = int(input("Enter marks obtained: "))
    #     writer.writerow([name, class1, marks])

    #     print("MENU:\n1. Enter New Student\n0. Exit")
    #     ans = int(input("Enter choice: "))

    #     if ans == 0:
    #         break
    reader = csv.reader(f)
    for i in reader:
        print(i)