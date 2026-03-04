class Student:
    def __init__(self, name, classsec, rollno, marks):
        self.name = name
        self.casssec = classsec
        self.rollno = rollno
        self.marks = marks
    def getname(self):
        print(self.name)
    @staticmethod
    def getinstitute(op=None):
        if (op != None):
            print(op)
        else:
            print("MSI")

s1 = Student("Apurva", "12A", 24, 89)
s2 = Student("Apurva Kumar", "3A", 48, 8.9)

s1.getname()
s2.getname()

Student.getinstitute()
s1.getinstitute("AP")
Student.getname(s1)

class Vehicle:
    def __init__(self,wheels = 4):
        self.wheels = wheels
    def wheelno(self):
        print(self.wheels)

class Car(Vehicle):
    def __init__(self,wheels,model = "TATA"):
        self.model = model
        super().__init__(wheels)
    def modelname(self):
        print(self.model)

class SportsCar(Car):
    def __init__(self,wheels,model,comp = "F1 Main"):
        self.comp = comp
        super().__init__(wheels,model)
    def tellcomp(self):
        print(self.comp)

f1 = SportsCar(5,"TOYOTA","F1 Race")
f1.modelname()
f1.tellcomp()
f1.wheelno()