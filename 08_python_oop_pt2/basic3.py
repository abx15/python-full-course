class Vhicle:
    def move(self):
        print("Moving")

class Car(Vhicle):
    def drive(self):
        print("driving a car")

class Ev(Car):
    def charge(self):
        print("charging a car")

Ev1 = Ev()
Ev1.move()       
Ev1.charge()       
