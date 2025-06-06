# Queue: First In First Out 

class Queue:
    def __init__(self):
        self.items = [] # Initialize an empty list to store queue items

    # Enqueue: Add an item to the rear of the queue
    def enqueue(self, item):
        # Append the item to the end of the queue
        self.items.append(item)

    # Dequeue: Remove item from the front of the queue
    def dequeue(self):
        if self.items :     # Check if the queue is not empty
            # Remove and return the first item from the queue
            return self.items.pop(0)
        else:
            return "Queue is empty"

    # Get the size of the queue
    def size(self):
        return len(self.items)

    # Display the queue
    def display(self):
        print("Queue:", self.items)


# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()               # Queue: [10, 20, 30]
print(q.dequeue())        # 10
q.display()               # Queue: [20, 30]
q.enqueue(40)             # Add 40 to the queue
q.display()               # Queue: [20, 30, 40]
print(q.dequeue())        # 20
print(q.dequeue())        # 30
q.display()               # Queue: [40]
print("Size:", q.size())  # 1

