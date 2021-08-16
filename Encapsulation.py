class Shape:
    def __init__(self,a):
        self.__a = a
    def get_a(self):
        return self.__a
    def set_a(self,b):
        self.__a = b
        return self.__a

class Rectangle(Shape):
    pass

a = Shape(5)
#print(a.__a)
print(a.get_a())
print(a.set_a(10))
