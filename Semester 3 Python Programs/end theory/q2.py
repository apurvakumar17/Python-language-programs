import pickle
with open("numbers.bin","wb") as fp:
    data = [10,20,30,40,50]
    pickle.dump(data,fp)
with open("numbers.bin","rb") as fp:
    dta = pickle.load(fp)
    print(type(dta))