import pickle
with open("home.bin","wb+") as f:
    pickle.dump("Hello",f)
    f.seek(0)
    dt=pickle.load(f)
    print(dt)