class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Using polymorphism
for animal in (Dog(), Cat()):
    print(animal.speak())
