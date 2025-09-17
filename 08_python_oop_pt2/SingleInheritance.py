# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} vehicle started")

# Child class
class Car(Vehicle):
    def honk(self):
        print(f"{self.brand} car honks! Beep Beep!")

# Usage
my_car = Car("Toyota")
my_car.start()   
my_car.honk()    
