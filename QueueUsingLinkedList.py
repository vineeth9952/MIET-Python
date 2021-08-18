'''
Queue
==>FIFO (FIRST IN FIRST OUT)
==>LILO (LAST IN LAST OUT)

Enqueue = Inserts value into the queue
Dequeue = deletes value from the queue
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class QueueUsingLinkedList(Node):
    def __init__(self):
        self.head = None
        self.last = None
    def Enqueue(self,x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            print(self.head.data,"is Enqueued")
        else:
            t = self.head
            while(t.next is not None):
                t = t.next

            t.next = new_node
            print(new_node.data, "is Enqueued")

    def Dequeue(self):
        if (self.head is None):
            print("no elements")
        else:
            print(self.head.data,"is Dequeued")
            self.head = self.head.next

    def Display(self):
        t = self.head
        while (t.next is not None):
            print(t.data, end=" ")
            t = t.next
        print(t.data)

q = QueueUsingLinkedList()
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)
q.Display()
q.Dequeue()
