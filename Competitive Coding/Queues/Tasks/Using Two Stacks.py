# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import deque

# q = int(input())
# queue = deque()
# for _ in range(q):
#     query = list(map(int, input().split()))
    
#     if query[0] == 1:
#         queue.append(query[1])
#     elif query[0] == 2:
#         queue.popleft()     
#     elif query[0] == 3:
#         print(queue[0])     


'''
q = int(input())
queue = []
queries = []
for i in range(q):
    queries.append(list(map(int, input().rstrip().split())))
    
for query in queries:
    # print(query)
    if query[0] == 1:
        queue.append(query[1])
    elif query[0] == 2:
        queue.pop(0)
    elif query[0] == 3:
        print(queue[0])
'''


class MyQueue:
    """
    Implements a queue using two stacks.
    Methods
    -------
    push(x):
        Pushes element x to the back of the queue.
    pop():
        Removes and returns the element from the front of the queue.
    peek():
        Returns the element at the front of the queue without removing it.
    empty():
        Returns True if the queue is empty, False otherwise.
    """
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.peek()
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

