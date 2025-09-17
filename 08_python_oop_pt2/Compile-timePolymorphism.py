# + works as addition for numbers and concatenation for strings
print(10 + 20)         # 30
print("Hello " + "World") # "Hello World"

# Custom operator overloading
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(150)
print(b1 + b2)  # 250
