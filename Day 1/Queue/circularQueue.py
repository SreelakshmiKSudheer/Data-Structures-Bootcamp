class CircularQueue:
    # Circular Queue: A linear data structure that uses a fixed-size buffer in a circular manner,
    # allowing efficient use of space by reusing freed positions.
    # front: points to the first element in the queue
    # rear: points to the last element in the queue

    def __init__(self, size):
        # Initialize the circular queue with a fixed size
        self.size = size
        self.queue = [None] * size  # Fixed-size list
        self.front = self.rear = -1    

    def enqueue(self, value):
        # Check if the queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow! Cannot insert ", value)
            return

        # First element to be inserted
        if self.front == -1:
            self.front = 0

        # Move rear to next position
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1: 
            # Queue is empty
            print("Queue Underflow! Cannot dequeue")
            return

        value = self.queue[self.front]
        # If the queue has only one element
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            # Move front to next position
            self.front = (self.front + 1) % self.size
        return value

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        print("Queue elements:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                # checking if the iteration has reached the end of the queue
                break
            i = (i + 1) % self.size
        print()

# example 
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)  # Queue is full after this
cq.enqueue(70)  # cannot insert this value

cq.display()  # Output: 10 20 30 40 50

print("Dequeued:", cq.dequeue())  # Output: Dequeued: 10
cq.enqueue(60)  # Works because of circular nature
cq.display()  # Output: 20 30 40 50 60

print("Dequeued:", cq.dequeue())  # Output: Dequeued: 20
print("Dequeued:", cq.dequeue())  # Output: Dequeued: 30
print("Dequeued:", cq.dequeue())  # Output: Dequeued: 40
print("Dequeued:", cq.dequeue())  # Output: Dequeued: 50
print("Dequeued:", cq.dequeue())  # Output: Dequeued: 60
print("Dequeued:", cq.dequeue())  # cannot dequeue because queue is empty
cq.display()    # empty queue

