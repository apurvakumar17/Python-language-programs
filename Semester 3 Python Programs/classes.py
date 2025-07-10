class Student:

    school_name = "soe"

    def __init__(self, student_name = None, marks = None):
        print("Constructor called")
        self.sname = student_name
        self.marks = marks

    def getmarks(self, ss2):
        print(self.marks)
        print(ss2)


s1 = Student("Apurva")
print(s1.sname)

s2 = Student("Anu")
print(s2.sname)

s3 = Student()
print(s3.sname)
print(s1.school_name, Student.school_name)

s4 = Student("Apu", 99)
s4.getmarks(56)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def getavg(self):
        print("Length of list", len(self.marks))
        return((self.marks[0] + self.marks[1] + self.marks[2]) / 3)
    
s1 = Student("Bad boy", [25, 50, 75])
print(f"Name: {s1.name}\nSubject 1: {s1.marks[0]}\nSubject 2: {s1.marks[1]}\nSubject 3: {s1.marks[2]}\nAverage: {s1.getavg()}")