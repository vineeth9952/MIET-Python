class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL(Node):
    def __init__(self):
        self.head = None
        self.last = None
    def InsertatEnd(self,x):
        temp = Node(x)
        if self.head is None:
            self.head = temp
        else:
            t = self.head
            while(t.next is not None):
                t = t.next

            t.next = temp

    def Display(self):
        t = self.head
        while (t.next is not None):
            print(t.data,end=" ")
            t = t.next
        print(t.data)

    def Rotate(self,x):
        if x==0:
            return

        temp = self.head
        count=1
        while(count<x and temp is not None):
            temp = temp.next
            count += 1

        if temp is None:
            return
        new_first = temp

        while (temp.next is not None):
            temp = temp.next

        temp.next = self.head
        self.head = new_first.next
        new_first.next = None

a = SLL()

a.InsertatEnd(10)
a.InsertatEnd(20)
a.InsertatEnd(30)
a.InsertatEnd(40)
a.InsertatEnd(50)
a.InsertatEnd(60)
a.InsertatEnd(70)

a.Display()
a.Rotate(9)
print("after rotation")
a.Display()