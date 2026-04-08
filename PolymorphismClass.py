class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "123")
boat1 = Boat("Boeing", "btt")
plane1 = Plane("skda", "wre")

all = car1, boat1, plane1
# for x in (car1, boat1, plane1):
#     x.move()

for x in all:
    x.move()