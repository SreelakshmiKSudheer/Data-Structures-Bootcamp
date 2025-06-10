# A Circular Singly Linked List is a variation of a singly linked list
# where the last node points back to the head, forming a circle.

# Step 1: Define the node class
class CNode:
    def __init__(self, data):         # Constructor to initialize the node
        self.data = data              # Store the data
        self.next = None              # Reference to the next node (default is None)

# Step 2: Define the circular singly linked list class
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None              # Start with an empty list (head is None)

    def insert_end(self, data):
        # Step 3: Create a new node with given data
        new_node = CNode(data)

        # Step 4: If the list is empty, point the node to itself
        if not self.head:             # If list is empty
            self.head = new_node      # Make new_node the head
            new_node.next = self.head # Point it to itself to form a single-node circle
            return                    # Exit after insertion

        # Step 5: Traverse the list to find the last node
        current = self.head
        while current.next != self.head:  # Loop until we reach the last node
            current = current.next

        current.next = new_node       # Link the last node to the new node
        new_node.next = self.head     # Point new_node's next to head to maintain circularity

    def display(self):
        # Step 6: Display all elements of the circular list
        if not self.head:             # If the list is empty
            print("List is empty")
            return

        current = self.head           # Start from the head node
        while True:                   # Infinite loop until we manually break it
            print(current.data, end=" -> ")  # Print the data
            current = current.next    # Move to the next node
            if current == self.head:  # If we're back at head, full circle completed
                break

        print("(Back to head)")       # Indicate circular nature

# Step 7: Using the circular singly linked list
cll = CircularSinglyLinkedList()      # Create empty circular list
cll.insert_end(5)                     # Insert 5
cll.insert_end(10)                    # Insert 10
cll.insert_end(15)                    # Insert 15
cll.display()                         # Output: 5 -> 10 -> 15 -> (Back to head)

# Time Complexity:
#   Insert at end: O(n), as we must find the last node
#   Display: O(n), as we visit each node once
# Space Complexity: O(n)
