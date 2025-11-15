class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)

student1 = Student("Apurva", 20)
student2 = Student("Shreyas", 21)

student1.display_info()
student2.display_info()

print("\nApurva, 04814902024")