# A Singly Linked List is a sequence of nodes where each node points to the next node.

# Step 1: Create the node class
class Node:
    def __init__(self, data):         # Constructor to initialize the node
        self.data = data              # Store the value/data
        self.next = None              # Initialize next pointer to None (no next node yet)

# Step 2: Create the Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None              # Start with an empty list, so head is None

    def insert_end(self, data):
        # Step 3: Create a new node with the given data
        new_node = Node(data)         # Create a node with the provided data

        # Step 4: Check if the list is empty
        if not self.head:             # If head is None, list is empty
            self.head = new_node      # Make new_node the first node (head)
            return                    # Exit after inserting the first node

        # Step 5: If list is not empty, find the last node
        current = self.head           # Start from the head node
        while current.next:           # Loop until we reach the last node
            current = current.next    # Move to the next node

        current.next = new_node       # Link last node's next to new_node

    def display(self):
        # Step 6: Display all nodes from head to end
        current = self.head           # Start from the head
        while current:                # Loop until we reach the end (None)
            print(current.data, end=" -> ")  # Print node's data
            current = current.next    # Move to the next node
        print("None")                 # Print None at the end to indicate end of list

# Step 7: Using the singly linked list
sll = SinglyLinkedList()              # Create an empty linked list
sll.insert_end(10)                    # Insert 10 at the end
sll.insert_end(20)                    # Insert 20 at the end
sll.insert_end(30)                    # Insert 30 at the end
sll.display()                         # Output: 10 -> 20 -> 30 -> None

# Time Complexity:
#   Insert at end: O(n), because we may have to traverse the entire list
#   Display: O(n), as we visit each node once
# Space Complexity: O(n) for storing n nodes
