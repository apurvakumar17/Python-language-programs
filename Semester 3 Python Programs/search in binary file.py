import pickle

with open("binary_emp.dat", "wb") as file:
    empd = [[1,"apurva"], [2,"shreyas"], [3,"anubhav"], [4,"rohit"]]
    pickle.dump(empd, file)

with open("binary_emp.dat", "rb") as filer:
    empd = pickle.load(filer)
    print(empd)
    name = input("Enter name to search:")
    for i in empd:
        if i[1].lower() == name.lower():
            print("DATA FOUND!")
            print(i)
            break
    else:
        print("Not Found!")