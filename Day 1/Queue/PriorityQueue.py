"""
Priority Queue Implementation in Python (using multiple queues)

This program simulates a priority queue using an array of queues.
Each priority level (e.g., 1 to N) has its own individual queue.
Elements are dequeued based on priority: lower priority number = higher importance.

Queue Behavior:
- Enqueue: User specifies the priority (1 to np), and an item is inserted in that queue.
- Dequeue: Removes item from the front of the highest priority queue that is not empty.
- Display: Prints all items in all priority queues in order.

Globals:
- pq : List of lists representing queues for each priority level.
- f : Front pointers for each priority queue.
- r : Rear pointers for each priority queue.
- np : Number of priority levels.
- size : Maximum size per individual queue.
"""

f = []     # Front pointers for each priority queue
r = []     # Rear pointers for each priority queue
pq = []    # List of queues for different priorities
np = 0     # Number of priority levels
size = 0   # Maximum size of each individual queue


def display():
    # Display all elements in the priority queues.
    print("\nQueue : ")
    for i in range(np):
        if f[i] != -1:
            for j in range(f[i], r[i] + 1):
                print(pq[i][j], end=" ")
        print()  # Separate each priority level visually
    print()


def enqueue():
    # Insert an item into the appropriate priority queue.
    global pq, f, r

    # Input validation for priority level
    while True:
        priority = int(input("\nEnter priority : "))
        if priority > np or priority < 1:
            print(f"Only {np} priorities allowed (1 to {np})!")
        else:
            break

    index = priority - 1  # Convert to 0-based index

    # Check for overflow in the selected priority queue
    if r[index] == size - 1:
        print(f"\nQueue overflow for priority {priority}")
    else:
        item = int(input("Enter item to insert : "))
        r[index] += 1
        pq[index][r[index]] = item

        # Initialize front index if this is the first insertion
        if f[index] == -1:
            f[index] = 0

        display()


def dequeue():
    # Remove an item from the front of the highest-priority non-empty queue.
    global f, r

    # Search for the highest-priority non-empty queue
    for i in range(np):
        if f[i] != -1:
            f[i] += 1  # Move front pointer forward

            # If queue becomes empty after dequeue, reset both pointers
            if f[i] > r[i]:
                f[i] = -1
                r[i] = -1

            display()
            break
    else:
        print("\nQueue underflow")  # All queues are empty


def main():
    # Driver function: handles menu input and initializes queues.
    global size, np, f, r, pq

    size = int(input("Enter size of each priority queue : "))
    np = int(input("Enter number of priorities : "))

    f = [-1] * np               # Initialize front pointers
    r = [-1] * np               # Initialize rear pointers
    pq = [[0] * size for _ in range(np)]  # Initialize 2D queue array

    while True:
        print("\nChoices : \n1. Insert item\n2. Delete item\n3. Exit")
        choice = int(input("Enter desired choice [1/2/3] : "))
        if choice == 1:
            enqueue()
        elif choice == 2:
            dequeue()
        elif choice == 3:
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
