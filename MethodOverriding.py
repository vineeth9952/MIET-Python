
class A:
    def show(self):
        print("Iam in class A")

class B(A):
    def show(self):
        print("Iam in class B")

a1 = B()
a1.show()