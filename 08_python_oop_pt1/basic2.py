class MobilePhone:
    mobileCount = 0

    def __init__(self, phoneName, phonePrice):
        self.brand = phoneName
        self.price = phonePrice
        MobilePhone.mobileCount += 1

    def showDetails(self):
        print(f"Brand Name: {self.brand} price{self.price}")


phone1 = MobilePhone("Realme 12 Pro 5G", 2600)
phone2 = MobilePhone("iPhone 15 Pro", 150000)
phone2 = MobilePhone("iPhone 17 Pro", 170000)
phone1.showDetails()
phone2.showDetails()

print(phone1.brand)
print(phone2.brand)

phone2.brand = "MI"
print(phone2.brand)

print("Total Mobiles:", MobilePhone.mobileCount)

