class Anand:
    def __init__(self):
        print("This is Anand")

    def Samsung(self):
        print("Samsung phone of Anand")

    def Scooter(self):
        print("scooter of Anand")


class vineeth(Anand):
    def __init__(self):
        super().__init__()
        print("This is vineeth")

    def oneplus(self):
        print("oneplus of vineeth")

    def bike(self):
        print("bike of vineeth")

class Arjun(vineeth):
    def __init__(self):
        print("This is Arjun")

    def Cartoy(self):
        print("car toy of Arjun")
a = Anand()
v = vineeth()

ar = Arjun()

ar.Cartoy()
ar.oneplus()
ar.bike()
ar.Samsung()