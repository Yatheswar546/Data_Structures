#Stack in Python using List

stack = []

def push():
    print("Enter Element:")
    ele = int(input())
    stack.append(ele)
    print(stack)
    
def pop():
    if len(stack)==0:
        print("Stack is Empty")
    else:
        ele = stack.pop()
        print("Removed Element",ele)
    print(stack)
    
def peek():
    print(stack[-1])
    
def size():
    print(len(stack))
    
def display():
    print(stack)
    
#n = int(input())
while True:
    print("Enter your choice:")
    print("1.Push 2.Pop 3.Peek 4.Size 5.Display 6.Stop")
    choice = int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        peek()
    elif choice==4:
        size()
    elif choice==5:
        display()
    elif choice==6:
        print(stack)
        break
    else:
        print("inValid Choice")