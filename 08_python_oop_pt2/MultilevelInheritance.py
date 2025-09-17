class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def honk(self):
        print("Car honks!")

class ElectricCar(Car):
    def charge(self):
        print("Electric Car is charging")

ecar = ElectricCar()
ecar.move()   # From Vehicle
ecar.honk()   # From Car
ecar.charge() # From ElectricCar
