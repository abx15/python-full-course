class Appliance:
    def powerOn(self):
        print("Appliance is On")


class Fan(Appliance):
    def rotate(self):
        print("Fan rotaring")


class AC(Appliance):
    def cool(self):
        print("Ac cooling")


f = Fan()
f.powerOn()
f.rotate()
a = AC()
a.powerOn()
a.cool()
