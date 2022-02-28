#Priority Queues in Python

queue = []

def enqueue():
    print("Enter Element:")
    ele = input()
    print("Enter Priority:")
    pri = int(input())
    queue.append((pri,ele,))
    queue.sort()
    
def dequeue():
    ele = queue.pop(0)
    print("Removed Element",ele)
    print(queue)
    
while True:
    print("Enter your choice:")
    print("1.Enqueue 2.Dequeue 3.Front 4.Rear 5.Display 6.Stop")
    choice = int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        print(queue[0])
    elif choice==4:
        print(queue[-1])
    elif choice==5:
        print(queue)
    elif choice==6:
        print(queue)
        break
    else:
        print("inValid Choice")