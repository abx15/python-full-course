class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):   # Car inherits Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def info(self):
        print(f"Car: {self.brand}, Model: {self.model}")

# Usage
c = Car("Toyota", "Fortuner")
c.info()
