#Queue from right to left in Python

queue = []

def enqueue():
    print("Enter Element:")
    ele = int(input())
    queue.insert(0,ele)
    print(queue)

def dequeue():
    ele = queue.pop()
    print("Removed Element:",ele)
    print(queue)

while True:
    print("Enter your choice:")
    print("1.Enqueue 2.Dequeue 3.Front 4.Rear 5. Display 6.Stop")
    choice = int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        print("Front Element:",queue[-1])
    elif choice==4:
        print("Rear Element:",queue[0])
    elif choice==5:
        print(queue)
    elif choice==6:
        print(queue)
        break
    else:
        print("inValid Choice")