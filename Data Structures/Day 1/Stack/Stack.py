# Create a stack with given capacity
class Stack:
    def __init__(self, cap):
        self.cap = cap
        self.top = -1   # points to last element inserted in stack
        self.a = [None] * cap

    def push(self, x):
        if self.top == self.cap - 1:      # check if stack is full
            print("Stack Overflow")
            return
        self.top += 1   #self.top = self.top + 1
        self.a[self.top] = x    # insert element at top of stack

    def pop(self):
        if self.top < 0:        # check if stack is empty
            print("Stack Underflow")
            return
        popped = self.a[self.top]   # get the top element
        self.top -= 1               # decrease top index
        print(popped, " popped from stack")
    
    def display(self):
        if self.top < 0:            # check if stack is empty
            print("Stack is empty")
            return
        print("Stack elements are:", end=" ")
        for i in range(self.top + 1):
            print(self.a[i], end=" ")   # print elements in stack
        print()


s = Stack(5)    # Example usage
s.display()     # Display empty stack
s.push(10)      # 10 pushed to stack
s.display()     # 10
s.push(20)      # 10 20
s.push(30)      # 10 20 30
s.display()     # 10 20 30
s.pop()         # 30 popped from stack
s.display()     # 10 20