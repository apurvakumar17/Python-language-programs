import csv

with open("homedata.csv","w+",newline="") as fr:
    writer = csv.writer(fr)
    writer.writerow(["A",1])
    writer.writerows([["B",2],["C",3]])
    fr.seek(0)
    reader = csv.reader(fr)
    for i in reader:
        print(i)