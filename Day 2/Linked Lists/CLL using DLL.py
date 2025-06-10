class CDNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = CDNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node.prev = new_node
            return
        last = self.head.prev
        last.next = new_node
        new_node.prev = last
        new_node.next = self.head
        self.head.prev = new_node

    def display(self):
        if not self.head:
            return
        cur = self.head
        while True:
            print(cur.data, end=" <-> ")
            cur = cur.next
            if cur == self.head:
                break
        print("(Back to head)")
