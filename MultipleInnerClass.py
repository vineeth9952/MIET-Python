class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
        self.mob = self.Mobile()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
        self.mob.show()

    class Laptop:
        def __init__(self):
            self.brand = "dell"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.ram, self.cpu)



    class Mobile:
        def __init__(self):
            self.brand = "Apple"
            self.color = "silver"

        def show(self):
            print(self.brand, self.color)

s1 = Student("kamil", 23)


s1.show()


#s1lap = Student.Laptop()