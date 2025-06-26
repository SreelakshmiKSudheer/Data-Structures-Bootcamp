class Queue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = -1 # points to the next item to dequeue
        self.rear = -1  # points to the last item enqueued

    def enqueue(self, item):
        if self.rear == self.capacity - 1:
            print("Queue is full (Overflow)")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = item
        print("Enqueued:", item)

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty (Underflow)")
            return
        item = self.queue[self.front]
        self.front += 1
        if self.front > self.rear:
            self.front = -1
            self.rear = -1
        print("Dequeued:", item)

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        print("Queue contents:", end=" ")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()

q = Queue(5)

q.enqueue(10)   # queue: 10
q.enqueue(20)   # queue: 10 20
q.enqueue(30)   # queue: 10 20 30
q.display()

q.dequeue()     # dequeue 10
q.display()     # Queue: [20, 30] 

q.enqueue(40)   # queue: 20 30 40
q.enqueue(50)   # queue: 20 30 40 50
q.enqueue(60)   # queue: 20 30 40 50 60
q.display()     # Queue: [20, 30, 40, 50, 60]
q.enqueue(70)   # Queue is full (Overflow)
q.dequeue()     # dequeue 20
q.display()     # Queue: [30, 40, 50, 60]
q.dequeue()     # dequeue 30
q.dequeue()     # dequeue 40
q.display()     # Queue: [50, 60]
q.dequeue()     # dequeue 50
q.dequeue()     # dequeue 60
q.display()     # Queue is empty
q.dequeue()     # Queue is empty (Underflow)