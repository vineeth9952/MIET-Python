class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CSLL(Node):
    def __init__(self):
        self.head = None
        self.last = None
    def InsertatEnd(self,x):
        temp = Node(x)

        if self.head is None:
            self.head = temp
        else:
            t = self.head
            end = self.head
            while(t.next is not end):
                t = t.next
            t.next = temp

        temp.next = self.head

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
            self.last = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.last.next = new_node
            self.head = new_node
            #self.last.next = self.head

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
        while (t.next is not self.head):
            print(t.data,end=" ")
            t = t.next
        print(t.data)


a = CSLL()

a.InsertatBegin(10)
a.InsertatBegin(20)
a.InsertatBegin(30)
a.InsertatBegin(40)

'''
n = int(input())
while(n>0):
    a.InsertatEnd(n)
    n = int(input())
'''
a.Display()

