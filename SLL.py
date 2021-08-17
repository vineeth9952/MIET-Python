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
    def InsertatEnd2(self,x):
        temp = Node(x)
        if self.head is None:
            self.head = temp
            self.last = temp
        else:
            self.last.next = temp
            self.last = temp


    def DeleteatEnd(self):
        t = self.head
        if self.head is not None:
            while(t.next.next is not None):
                t=t.next
            t.next = None

    def InsertatBegin(self,x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def DeleteatBegin(self):
        if (self.head is None):
            print("no elements")
        else:
            self.head = self.head.next

    def InsertatPos(self,x,pos):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
        else:
            t = self.head
            while(pos-2):
                t = t.next
                pos -= 1

            new_node.next = t.next
            t.next = new_node

    def DeletionatPos(self,pos):
        if self.head is None:
            print("NO elements")
            return
        elif pos == 1:
            self.head = self.head.next
        else:
            t = self.head
            while(pos-2):
                t = t.next
                pos -= 1
                if (t.next is None):
                    print("Out of Range")
                    return

            t.next = t.next.next

    def Display(self):
        t = self.head
        while (t.next is not None):
            print(t.data,end=" ")
            t = t.next
        print(t.data)


a = SLL()
'''
a.InsertatEnd(10)
a.InsertatEnd(20)
a.InsertatEnd(30)
a.InsertatEnd(40)
a.InsertatEnd(50)
'''
n = int(input())
while(n>0):
    a.InsertatEnd(n)
    n = int(input())

a.Display()
a.DeletionatPos(6)
a.Display()