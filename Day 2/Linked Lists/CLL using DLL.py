# A Circular Doubly Linked List is a doubly linked list where
# the last node links back to the head, and the head’s prev links to the last node.

# Step 1: Define the node class
class CDNode:
    def __init__(self, data):         # Constructor to initialize node
        self.data = data              # Store the data
        self.prev = None              # Reference to previous node
        self.next = None              # Reference to next node

# Step 2: Define the circular doubly linked list class
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None              # Start with an empty list

    def insert_end(self, data):
        # Step 3: Create a new node with given data
        new_node = CDNode(data)

        # Step 4: If list is empty, point new_node to itself both ways
        if not self.head:             
            self.head = new_node              # Make new_node the head
            new_node.next = new_node          # Point next to itself (circular)
            new_node.prev = new_node          # Point prev to itself (circular)
            return

        # Step 5: Get the last node (head.prev in circular DLL)
        last = self.head.prev                 # Previous of head is last node

        last.next = new_node                  # Set current last node's next to new_node
        new_node.prev = last                  # Link new_node’s prev to last node
        new_node.next = self.head             # new_node's next points to head
        self.head.prev = new_node             # Head's prev updated to new last node

    def display(self):
        # Step 6: Display elements in circular doubly linked list
        if not self.head:                     # Check if list is empty
            print("List is empty")
            return

        current = self.head                   # Start from head
        while True:
            print(current.data, end=" <-> ")  # Print node data
            current = current.next            # Move forward
            if current == self.head:          # If we return to head, stop
                break
        print("(Back to head)")               # Indicate circular connection

# Step 7: Using the circular doubly linked list
cdll = CircularDoublyLinkedList()            # Create empty CDLL
cdll.insert_end(1)                           # Insert 1
cdll.insert_end(2)                           # Insert 2
cdll.insert_end(3)                           # Insert 3
cdll.display()                               # Output: 1 <-> 2 <-> 3 <-> (Back to head)

# Time Complexity:
#   Insert at end: O(1), if we use head.prev trick
#   Display: O(n), visits each node once
# Space Complexity: O(n)
