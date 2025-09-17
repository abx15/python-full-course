class ElectronicDevice:
    def powerOn(self):
        print("Powering On")


class Laptop(ElectronicDevice):
    def code(self):
        print("Code Start")


Laptop1 = Laptop()

Laptop1.powerOn()
Laptop1.code()
