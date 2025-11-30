class Student:
    def __init__(self, name, classsec, rollno, marks):
        self.name = name
        self.casssec = classsec
        self.rollno = rollno
        self.marks = marks
    def getname(self):
        print(self.name)
    @staticmethod
    def getinstitute():
        print("MSI")

s1 = Student("Apurva", "12A", 24, 89)
s2 = Student("Apurva Kumar", "3A", 48, 8.9)

s1.getname()
s2.getname()

Student.getinstitute()