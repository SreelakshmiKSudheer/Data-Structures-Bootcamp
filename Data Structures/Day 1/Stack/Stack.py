# Create a stack with given capacity
class Stack:
    def __init__(self, cap):
        self.cap = cap
        self.top = -1   # points to last element inserted in stack
        self.a = [None] * cap

    def push(self, x):
        if self.top == self.cap - 1:
            print("Stack Overflow")
            return
        self.top += 1   #self.top = self.top + 1
        self.a[self.top] = x  

    def pop(self):
        if self.top < 0:
            print("Stack Underflow")
            return
        popped = self.a[self.top]
        self.top -= 1
        print(popped, " popped from stack")
    
    def display(self):
        if self.top < 0:
            print("Stack is empty")
            return
        print("Stack elements are:", end=" ")
        for i in range(self.top + 1):
            print(self.a[i], end=" ")
        print()


s = Stack(5)
s.push(10)
s.display()
s.push(20)
s.push(30)
s.display()
s.pop()
s.display()