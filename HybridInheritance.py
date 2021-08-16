class Anand:
    def __init__(self):
        print("This is Anand")

    def Samsung(self):
        print("Samsung phone of Anand")

    def Scooter(self):
        print("scooter of Anand")

class Lalitha():
    def __init__(self):
        print("This is Lalitha")

    def Iphone(self):
        print("Apple of Lalitha")


class vineeth(Anand):
    def __init__(self):
        print("This is vineeth")

    def oneplus(self):
        print("oneplus of vineeth")

    def bike(self):
        print("bike of vineeth")

class Teja(Lalitha,Anand):
    def __init__(self):
        print("This is Teja")

    def Apple(self):
        print("Apple of Teja")

    def car(self):
        print("car of teja")

a = Anand()
v = vineeth()

t = Teja()


t.Apple()
t.car()
t.Samsung()
t.Scooter()
t.Iphone()