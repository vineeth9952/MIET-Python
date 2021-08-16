
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        a = self.m1 + other.m1
        b = self.m2 + other.m2
        t = Student(a,b)
        return t

    def __gt__(self, other):
        a = self.m1 + self.m2
        b = other.m1 + other.m2
        if (a>b):
            return True
        else:
            return False

    def __str__(self):
        return self.m1,self.m2
        #return '{}{}'.format(self.m1,self.m2)

s1 = Student(78,96)
s2 = Student(86,84)

a = "smart"
print(a)
print(s1)

if (s1>s2):
    print("s1 is greater")
else:
    print("s2 is greater")
