import pickle

student_data = {
    "name": "Apurva",
    "age": 20,
    "course": "BCA",
    "marks": [85, 90, 92]
}

with open("practical26_student.dat", "wb") as file:
    pickle.dump(student_data, file)
    print("Data written to binary file using dump().")

with open("practical26_student.dat", "rb") as file:
    loaded_data = pickle.load(file)
    print("\nData read from binary file using load():")
    print(loaded_data)
print("\nApurva Kumar, 04814902024")