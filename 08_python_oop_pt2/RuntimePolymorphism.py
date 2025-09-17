class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying")

# Polymorphism
for v in (Vehicle(), Car(), Plane()):
    v.move()
