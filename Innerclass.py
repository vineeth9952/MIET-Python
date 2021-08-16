class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()


    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "dell"
            self.cpu = "i5"
            self.ram = 16

        def show(self):
            print(self.brand, self.ram, self.cpu)


s1 = Student("kamil", 23)
s2 = Student("suvrat", 39)

s1.show()
Student.show(s2)

s1lap = Student.Laptop()