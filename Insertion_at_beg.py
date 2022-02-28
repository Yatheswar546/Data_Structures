#Linked List Insertion at the beginning in Python

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
    
    
ll = LinkedList()
n = int(input("Enter length of LinkedList:"))
for i in range(n):
    num = int(input("Enter number:"))
    ll.add_begin(num)

ll.printll()