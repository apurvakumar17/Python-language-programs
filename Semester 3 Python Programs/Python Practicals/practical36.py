# import pickle

# employees = [
#     {"id": 101, "name": "Apurva", "salary": 50000},
#     {"id": 102, "name": "Shreyas", "salary": 55000},
#     {"id": 103, "name": "Raju", "salary": 48000}
# ]

# with open("practical36_employees.dat", "wb") as f:
#     pickle.dump(employees, f)

#run this first time (once)

import pickle
try:
    with open("practical36_employees.dat", "rb") as file:
        employees = pickle.load(file) 
except FileNotFoundError:
    print("Error: employees.dat file not found!")
    exit()

search_name = input("Enter employee name to search: ").strip()

found = False
for emp in employees:
    if emp["name"].lower() == search_name.lower():
        print("\nEmployee Record Found:")
        print(emp)
        found = True
        break

if not found:
    print("Employee not found!")
print("\nApurva Kumar, 04814902024")