from abc import ABC,abstractmethod

class Student(ABC):
    @abstractmethod
    def name(self):
        pass

    def age(self):
        print("age = 22")

class firstyear(Student):
    def name(self):
        print("Conroe")

class secondyear(Student):
    def name(self):
        print("Skipper")

class thirdyear(Student):
    def name(self):
        print("KL Rahul")

s = thirdyear()
s.name()
s.age()
