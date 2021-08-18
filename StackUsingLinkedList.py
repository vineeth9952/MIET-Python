'''
STACK = It is a Linear DAta structure
Follows LIFO(LAST IN FIRST OUT)
        FILO(FIRST IN LAST OUT)

EMPTY() :- returns if stack is empty
size() :- return size of stack
peek()/top() :- return the top most element
push() :- inserts an element at the top in the stack
pop() :- deletes the topmost element

stack using list
stack using collections
stack using linkedlist
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class StackUsingLinkedlist(Node):
    def __init__(self):
        self.head = None
        self.size = 0

    def Push(self,x):
        new_node = Node(x)

        if self.head is None:
            self.head = new_node
            print(self.head.data," is Pushed")
        else:
            new_node.next = self.head
            self.head = new_node
            print(self.head.data, " is Pushed")

        self.size += 1
    def Pop(self):
        if self.head is None:
            print("Stack is Empty")
            return
        else:
            poppeditem = self.head.data
            print(poppeditem," is popped")
            self.head = self.head.next
        self.size -= 1

    def peek(self):
        if self.head is None:
            Exception("Stack is empty")
        else:
            return self.head.data

    def isEmpty(self):
        if (self.head is None):
            return True

    def sizeofstack(self):
        return self.size

    def Display(self):
        t = self.head
        while (t.next is not None):
            print(t.data, end=" ")
            t = t.next
        print(t.data)


s = StackUsingLinkedlist()

s.Push(10)
s.Push(20)
s.Push(30)
s.Push(40)
print("before popping")

print("Stack :- ",end=" ")
s.Display()
s.Pop()
print("After Popping")
print("Stack :- ",end=" ")
s.Display()

print("top element is ",s.peek())
print("size of stack is ",s.sizeofstack())











