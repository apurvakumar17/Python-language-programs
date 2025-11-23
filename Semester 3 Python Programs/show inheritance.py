class Animal:
    def sound(self):
        print("I am animal")

class Dog(Animal):
    def soundnew(self):
        print("I am Doggie")


a1 = Animal()
a1.sound()

d1 = Dog()
d1.soundnew()
d1.sound()