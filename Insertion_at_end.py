#Linked List Insertion at the End in Python

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
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
ll = LinkedList()
n = int(input("Enter length of LinkedList:"))
for i in range(n):
    num = int(input("Enter number:"))
    ll.add_end(num)

ll.printll()