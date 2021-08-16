


class Student:
    def sum(self,a=None,b=None,c=None):
        s = 0
        if (a!=None and b!=None and c!=None):
            s = a+b+c
        elif (a!=None and b!=None):
            s = a+b
        else:
            s = a
        return s
s1 = Student()
print(s1.sum(5,6,7))
print(s1.sum(5,6))
print(s1.sum(5))