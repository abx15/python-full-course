class Engine:
    def start_engine(self):
        print("Engine started")

class MusicSystem:
    def play_music(self):
        print("Playing music")

class Car(Engine, MusicSystem):
    pass

my_car = Car()
my_car.start_engine()
my_car.play_music()
