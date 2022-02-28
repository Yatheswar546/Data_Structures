#Insertions in a Linked List in Python

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
    
class LinkedList:
    def __init__(self):
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
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node        
    
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
            
    def add_after(self,data,x):
        new_node = Node(data)
        if self.head is None:
            print("Linked List is empty!!!")
            return
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Element is not Found!!!")
        else:
            new_node.ref = n.ref
            n.ref = new_node        
    
ll = LinkedList()
while True:
    print("1.Insertion at Beginning\n2.Insertion at End\n3.Insertion Before a Node\n4.Insertion After a Node\n5.Display\n6.Stop")
    choice = int(input("Enter your choice:"))
    if choice==1:
        num=int(input("Enter number"))
        ll.add_begin(num)
        ll.printll()
    elif choice==2:
        num=int(input("Enter number"))
        ll.add_end(num)
        ll.printll()
    elif choice==3:    
        data = int(input("Enter the element to be inserted:"))  
        x = int(input("Before which the number the element is to be inserted:"))
        ll.add_before(data,x)
        ll.printll()
    elif choice==4:
        data = int(input("Enter the element to be inserted:"))  
        x = int(input("After which the number the element is to be inserted:"))
        ll.add_after(data,x)
        ll.printll()
    elif choice==5:
        ll.printll()
    elif choice==6:
        break
    else:
        print("inValid Choice!!!!!!")