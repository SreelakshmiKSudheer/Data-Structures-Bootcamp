# A Doubly Linked List is similar to a Singly Linked List,
# but each node has references to both the next and the previous node.

# Step 1: Define the node for a doubly linked list
class DNode:
    def __init__(self, data):         # Constructor to initialize node
        self.data = data              # Store the data
        self.prev = None              # Reference to the previous node (None initially)
        self.next = None              # Reference to the next node (None initially)

# Step 2: Define the doubly linked list class
class DoublyLinkedList:
    def __init__(self):
        self.head = None              # Initially, the list is empty (head is None)

    def insert_end(self, data):
        # Step 3: Create a new node with the given data
        new_node = DNode(data)

        # Step 4: If list is empty, make new node the head
        if not self.head:             # If head is None
            self.head = new_node      # Assign new node as the head
            return                    # Exit after insertion

        # Step 5: If list is not empty, find the last node
        current = self.head           # Start from the head
        while current.next:           # Traverse to the last node
            current = current.next    # Move to the next node

        current.next = new_node       # Set last node's next to new node
        new_node.prev = current       # Set new node's prev to current (backward link)

    def display(self):
        # Step 6: Display all nodes in forward direction
        current = self.head           # Start from head
        while current:                # Loop until we reach the end
            print(current.data, end=" <-> ")  # Print node's data with double arrow
            current = current.next    # Move to the next node
        print("None")                 # End of list

# Step 7: Using the doubly linked list
dll = DoublyLinkedList()              # Create an empty DLL
dll.insert_end(100)                   # Insert 100 at the end
dll.insert_end(200)                   # Insert 200 at the end
dll.insert_end(300)                   # Insert 300 at the end
dll.display()                         # Output: 100 <-> 200 <-> 300 <-> None

# Time Complexity:
#   Insert at end: O(n), as we may need to traverse the list
#   Display: O(n), to visit each node
# Space Complexity: O(n), one node object for each element
