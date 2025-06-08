def display(q, front, rear):  # Display queue contents
    print("\nContents rn :", end=" ")
    for i in range(front, rear + 1):
        print(q[i], end="  ")
    print()

def rear_enqueue(q, front, rear, size):  # Insert from rear
    if rear[0] == size - 1:
        print("\nQueue overflow")
    else:
        rear[0] += 1
        item = int(input("\nEnter item to be inserted: "))
        q[rear[0]] = item

        if rear[0] == 0:
            front[0] = 0

        display(q, front[0], rear[0])

def front_dequeue(q, front, rear, size):  # Delete from front
    if front[0] > rear[0] or front[0] == -1:
        print("\nQueue underflow")
    else:
        front[0] += 1
        if front[0] > rear[0]:
            front[0] = rear[0] = -1
            print("\nQueue is now empty")
        else:
            display(q, front[0], rear[0])

def front_enqueue(q, front, rear, size):  # Insert from front
    if front[0] <= 0:
        print("\nQueue overflow")
    else:
        front[0] -= 1
        item = int(input("\nEnter item to be inserted: "))
        q[front[0]] = item

        display(q, front[0], rear[0])

def rear_dequeue(q, front, rear, size):  # Delete from rear
    if front[0] > rear[0] or rear[0] < 0:
        print("\nQueue underflow")
    else:
        rear[0] -= 1
        if front[0] > rear[0]:
            front[0] = rear[0] = -1
            print("\nQueue is now empty")
        else:
            display(q, front[0], rear[0])

def main():
    size = int(input("Enter size of queue: "))
    q = [0] * size
    front = [-1]  # Using list so we can pass by reference
    rear = [-1]

    print("\nChoices:\n1. Front enqueue\n2. Front dequeue\n3. Rear enqueue\n4. Rear dequeue\n5. Exit")

    while True:
        choice = int(input("Give the desired choice[1/2/3/4/5]: "))
        if choice == 1:
            front_enqueue(q, front, rear, size)
        elif choice == 2:
            front_dequeue(q, front, rear, size)
        elif choice == 3:
            rear_enqueue(q, front, rear, size)
        elif choice == 4:
            rear_dequeue(q, front, rear, size)
        elif choice == 5:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
