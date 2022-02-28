#Queue from left to right in Python

queue = []

def enqueue():
    print("Enter Element:")
    ele = int(input())
    queue.append(ele)
    print(queue)

def dequeue():
    if not queue:
        print("Empty")
    else:    
        ele = queue.pop(0)
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
        print("Front Element:",queue[0])
    elif choice==4:
        print("Rear Element:",queue[-1])
    elif choice==5:
        print(queue)
    elif choice==6:
        print(queue)
        break
    else:
        print("inValid Choice")