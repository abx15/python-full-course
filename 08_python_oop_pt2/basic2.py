class Camera:
    def takePhoto(self):
        print("Taking Pic")


class Phone:
    def makeCall(self):
        print("Call Someone")


class smartPhone(Camera, Phone):
    pass


phone1 = smartPhone()
phone1.makeCall()
phone1.takePhoto()