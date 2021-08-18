class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class SLL(Node):
    def __init__(self):
        self.head = None
        self.last = None
    def InsertatEnd(self,x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            new_node.prev = self.head
            new_node.next = self.head

        else:
            t = self.head
            end = self.head
            while(t.next is not end):
                t = t.next

            t.next = new_node
            new_node.prev = t
            new_node.next = self.head
            self.head.prev = new_node

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
            self.head.prev = new_node
            self.head = new_node

    def DeleteatBegin(self):
        if (self.head is None):
            print("no elements")
        else:
            self.head = self.head.next
            self.head.prev = None

    def DeletionatPos(self,pos):
        if self.head is None:
            print("NO elements")
            return
        elif pos == 1:
            self.head = self.head.next
            self.head.prev = None
        else:
            t = self.head
            while(pos-2):
                t = t.next
                pos -= 1
                if (t.next is None):
                    print("Out of Range")
                    return

            t.next = t.next.next
            t.next.prev = t


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
            new_node.prev = t
            t.next = new_node

    def Display(self):
        t = self.head
        while (t.next is not self.head):
            print("node.prev=",t.prev,"node.data=",t.data,"node address=",hex(id(t)),"node.next=",hex(id(t.next)))
            #print(t.data,end=" ")
            t = t.next
        #print(t.data)
        print("node.prev=", hex(id(t.prev)), "node.data=", t.data, "node address=", hex(id(t)), "node.next=", t.next)


a = SLL()

a.InsertatEnd(10)
a.InsertatEnd(20)
a.InsertatEnd(30)
a.InsertatEnd(40)
a.InsertatEnd(50)
a.InsertatEnd(60)
a.InsertatEnd(70)

a.Display()