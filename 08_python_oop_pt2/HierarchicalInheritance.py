class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def honk(self):
        print("Car honks!")

class Bike(Vehicle):
    def wheelie(self):
        print("Bike does a wheelie!")

c = Car()
b = Bike()
c.move()
b.move()
