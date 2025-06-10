class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = new_node
        new_node.next = self.head

    def display(self):
        if not self.head:
            return
        cur = self.head
        while True:
            print(cur.data, end=" -> ")
            cur = cur.next
            if cur == self.head:
                break
        print("(Back to head)")
