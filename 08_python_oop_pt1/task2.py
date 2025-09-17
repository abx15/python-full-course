# Design a class Laptop with attributes like brand model and price. Add a method apply_discount() that reduces the price by 10%


class Laptop:
    def __init__(self, brand, model, price):
        self.brandName = brand
        self.brandModel = model
        self.brandPrice = price

    def applyDiscount(self):
        print(f"Brand Name: {self.brandName}")
        print(f"Brand Model: {self.brandModel}")
        print(f"Brand Price: {self.brandPrice}")
        print(f"Discount Price: {self.brandPrice*0.10}")
        print(f"Total Price: {self.brandPrice- self.brandPrice*0.10}")

laptop1 = Laptop("Asus", "Tuf Gaming", 70000 )
laptop1.applyDiscount()