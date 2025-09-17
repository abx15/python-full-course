class Dog:
    def sound(self):
        return "Woof"

class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Moo"

# Polymorphism in action
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.sound())
