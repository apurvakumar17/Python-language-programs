import pickle

dt = {"name":"Apurva", "Class":12, "Roll No.": 24}
with open("dt.dat", "wb") as filew:
    pickle.dump(dt, filew)

with open("dt.dat","rb") as filer:
    x = pickle.load(filer)
    print(x)