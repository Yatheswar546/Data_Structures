#Linked List Insertion at a Particular Position
#Case 1: Insertion Before a Specific Node

class Node:
    def _init_(self,data):
        self.data = data
        self.ref = None
    
class LinkedList:
    def _init_(self):
        self.head = None
        
    def printll(self):
        if self.head == None:
            print("Linked List is empty!!!")
        else:
            n = self.head
            while n.ref is not None:
                print(n.data,"--->",end=" ")
                n = n.ref
            print(n.data)    
    
    def add_begin(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:    
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node        
    
    def add_before(self,data,x):
        new_node = Node(data)
        if self.head is None:
            print("Linked List is Empty!!!")
            return
        if self.head.data == x:
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Element is not Found!!!")
        else:    
            new_node.ref = n.ref
            n.ref = new_node
            
    
ll = LinkedList()
n = int(input("Enter length of LinkedList:"))
for i in range(n):
    num = int(input("Enter number:"))
    ll.add_begin(num)

ll.printll()
data = int(input("Enter the element to be inserted:"))
x = int(input("Before which the number the element is to be inserted:"))
ll.add_before(data,x)
ll.printll()