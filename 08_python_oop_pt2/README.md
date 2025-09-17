# Advanced OOP Notes – Python

This repository contains **comprehensive notes on Advanced Object-Oriented Programming (OOP)** in Python. It is designed for developers who want to strengthen their OOP skills and understand real-world applications.

---

## **Key Concepts Covered**

### **1. Inheritance**
- **Definition:** Mechanism to create a new class from an existing class.
- **Purpose:** Code reuse and hierarchical modeling.
- **Types:**
  - Single Inheritance
  - Multiple Inheritance
  - Multilevel Inheritance
  - Hierarchical Inheritance
- **Example:**
```python
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def play_music(self):
        print("Playing music")

my_car = Car()
my_car.start()        # Vehicle started
my_car.play_music()   # Playing music
```

- - - Real-World: Cars, bikes inherit common properties from Vehicle.

### 2. Encapsulation

- Definition: Restrict access to class attributes and provide controlled access via methods.

- Purpose: Protect sensitive data.

 **Example:**
```python

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500

```
- - - Real-World: Bank account balance should not be directly accessible.

### 3. Polymorphism

- Definition: Ability of an object to take multiple forms.

- Purpose: Methods can behave differently depending on the object.

**Example:**
```python

class Bird:
    def fly(self):
        print("Some birds can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguins can't fly")

p = Penguin()
p.fly()  # Penguins can't fly

```
- - - Real-World: Payment methods (UPI, PayPal, Credit Card) share the same method name pay() but behave differently.

### 4. Abstraction

- Definition: Hiding internal implementation details and exposing only functionality.

- Purpose: Focus on what an object does, not how.

**Example:**
```python

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())  # 78.5

```
- - - Real-World: Shape’s formula is abstract; each shape (Circle, Rectangle) implements its own formula.

### 5. Magic / Dunder Methods

- Definition: Special methods with double underscores (__) to customize object behavior.

**Common Methods:**

- __init__() – constructor

- __str__() – string representation

- __add__() – overload + operator

**Example:**
```python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1,2)
p2 = Point(3,4)
print(p1 + p2)  # (4, 6)

```
- - - Real-World: Operator overloading, customized print behavior.

### 6. Composition

- Definition: “Has-a” relationship between classes.

**Example:**
```python

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started")

c = Car()
c.start()
```

- - Real-World: A Car has an Engine, a House has a Room.

## 7. Class & Static Methods

- @classmethod: Operates on the class itself.

- @staticmethod: Independent of class and instance.
```python

class MyClass:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def greet():
        print("Hello!")

MyClass.increment()
print(MyClass.count)  # 1
MyClass.greet()       # Hello!
```
### 8. Property Decorators

- Pythonic way to create getters and setters.
```python

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value

e = Employee("Arun", 5000)
e.salary = 6000
print(e.salary)  # 6000
```
## Best Practices

- Prefer composition over deep inheritance.

- Keep attributes private if they shouldn’t be accessed directly.

- Use abstract classes for common interfaces.

- Leverage magic methods for custom behavior.

## Real-World Applications

- Banking System → Encapsulation for account balances.

- Online Store → Polymorphism for payment methods.

- Game Development → Inheritance for characters (Player, Enemy).

- GUI Application → Composition for widgets (Button, Label, TextBox).

