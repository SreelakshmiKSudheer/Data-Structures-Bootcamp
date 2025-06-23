"""
Double-Ended Queue (Deque) Implementation in Python

This program implements a linear double-ended queue using a fixed-size array.
It supports the following operations:

1. Front Enqueue: Insert an element at the front end of the queue.
2. Front Dequeue: Remove an element from the front end.
3. Rear Enqueue: Insert an element at the rear end of the queue.
4. Rear Dequeue: Remove an element from the rear end.
5. Display: Print elements from front to rear.

Implementation Notes:
- The queue is represented as a list of fixed size.
- `front` and `rear` are passed as single-item lists to simulate pass-by-reference.
- Queue overflow occurs if no space is available at the intended end.
- Queue underflow occurs if trying to remove from an empty queue.
"""

def display(q, front, rear):
    # Display the current contents of the queue.
    print("\nContents rn :", end=" ")
    for i in range(front, rear + 1):
        print(q[i], end="  ")
    print()


def rear_enqueue(q, front, rear, size):
    # Insert an element at the rear end of the queue.
    if rear[0] == size - 1:
        print("\nQueue overflow")
    else:
        rear[0] += 1
        item = int(input("\nEnter item to be inserted: "))
        q[rear[0]] = item

        if rear[0] == 0:
            front[0] = 0

        display(q, front[0], rear[0])


def front_dequeue(q, front, rear, size):
    # Remove an element from the front end of the queue.
    if front[0] > rear[0] or front[0] == -1:
        print("\nQueue underflow")
    else:
        front[0] += 1
        if front[0] > rear[0]:
            front[0] = rear[0] = -1
            print("\nQueue is now empty")
        else:
            display(q, front[0], rear[0])


def front_enqueue(q, front, rear, size):
    # Insert an element at the front end of the queue.
    if front[0] <= 0:
        print("\nQueue overflow")
    else:
        front[0] -= 1
        item = int(input("\nEnter item to be inserted: "))
        q[front[0]] = item

        display(q, front[0], rear[0])


def rear_dequeue(q, front, rear, size):
    # Remove an element from the rear end of the queue.
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
    # Main driver function for the deque operations menu.
    size = int(input("Enter size of queue: "))
    q = [0] * size
    front = [-1]
    rear = [-1]

    print("\nChoices:\n1. Front enqueue\n2. Front dequeue\n3. Rear enqueue\n4. Rear dequeue\n5. Exit")

    while True:
        choice = int(input("Give the desired choice [1/2/3/4/5]: "))
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
