# 📘 Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of **objects** and **classes**.  
Python supports OOP, making it easier to write modular, reusable, and maintainable code.

---

## 🔑 Key OOP Concepts in Python

### 1. **Class**

A class is a **blueprint** for creating objects.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show(self):
        print(f"Car: {self.brand} {self.model}")
```

### 2. Object

An object is an instance of a class.

```python
car1 = Car("Toyota", "Fortuner")
car2 = Car("Tesla", "Model X")

car1.show()  # Car: Toyota Fortuner
car2.show()  # Car: Tesla Model X
```

### 3. Encapsulation

Encapsulation means hiding internal details and exposing only necessary things.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500
```

### 4. Inheritance

Inheritance allows one class to inherit properties and methods from another.

```python
class Animal:
    def speak(self):
        print("This is an animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof Woof!")

dog = Dog()
dog.speak()  # Woof Woof!
```

### 5. Polymorphism

Polymorphism means the same method can behave differently depending on the object.

```python
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

def make_sound(animal):
    animal.speak()

make_sound(Cat())   # Meow
make_sound(Dog())   # Woof
```

### 6. Abstraction

Abstraction means hiding implementation details and showing only the necessary features.
In Python, we use the abc module to implement abstraction.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

circle = Circle(5)
print(circle.area())  # 78.5
```

## 📝 Summary

- **Class** → Blueprint for objects

- **Object** → Instance of a class

- **Encapsulation** → Hides internal details

- **Inheritance** → Reuse code from parent class

- **Polymorphism** → Same method, different behavior

- **Abstraction** → Hides implementation

# 🚀 Real-World Example: Student Management

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}")

student1 = Student("Arun", 20, "S101")
student1.show()
```
