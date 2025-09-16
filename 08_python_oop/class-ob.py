class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")

# Creating objects
s1 = Student("Arun", 101)
s2 = Student("Rahul", 102)

s1.show()
s2.show()
