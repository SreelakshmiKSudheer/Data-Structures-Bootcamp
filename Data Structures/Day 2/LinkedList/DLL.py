class Node:
    def __init__(self, data):  # Constructor to initialize the node
        self.data = data        # Store the value/data
        self.next = None        # Initialize next pointer to None
        self.prev = None        # Initialize previous pointer to None

class DoublyLinkedList:
    def __init__(self):
        self.head = None        # Start with an empty list, so head is None
        self.tail = None        # Also keep track of the tail for O(1) end operations

    def insert_beginning(self, data):
        # Step 3: Create a new node with the given data
        new_node = Node(data)

        # Step 4: If the list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # Step 5: If the list is not empty
        else:
            new_node.next = self.head  # New node's next points to current head
            self.head.prev = new_node  # Current head's prev points to new node
            self.head = new_node       # Update head to the new node
        print(f"Inserted {data} at the beginning.")

    def insert_end(self, data):
        # Step 3: Create a new node with the given data
        new_node = Node(data)

        # Step 4: If the list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # Step 5: If the list is not empty
        else:
            new_node.prev = self.tail  # New node's prev points to current tail
            self.tail.next = new_node  # Current tail's next points to new node
            self.tail = new_node       # Update tail to the new node
        print(f"Inserted {data} at the end.")

    def insert_at_arbitrary_position(self, data, position):
        # Step 3: Handle invalid position (less than 1)
        if position < 1:
            print("Position should be 1 or greater.")
            return

        new_node = Node(data) # Create a new node

        # Step 4: If inserting at the beginning (position 1)
        if position == 1:
            self.insert_beginning(data) # Reuse insert_beginning
            return

        # Step 5: Traverse to the node *before* the desired position
        current = self.head
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1

        # Step 6: Check if the position is out of bounds
        if not current:
            print(f"Position {position} is out of bounds. List has fewer than {position-1} elements.")
            return

        # Step 7: If inserting at the very end
        if not current.next:
            self.insert_end(data) # Reuse insert_end
            return

        # Step 8: Insert the new node between current and current.next
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        print(f"Inserted {data} at position {position}.")

    def delete_beginning(self):
        # Step 3: Check if the list is empty
        if not self.head:
            print("List is empty, cannot delete from the beginning.")
            return None

        # Step 4: Store the data of the node to be deleted
        deleted_data = self.head.data

        # Step 5: If there's only one node in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # Step 6: If there are multiple nodes
        else:
            self.head = self.head.next  # Move head to the next node
            self.head.prev = None       # The new head's prev is now None
        print(f"Deleted {deleted_data} from the beginning.")
        return deleted_data

    def delete_end(self):
        # Step 3: Check if the list is empty
        if not self.head:
            print("List is empty, cannot delete from the end.")
            return None

        # Step 4: Store the data of the node to be deleted
        deleted_data = self.tail.data

        # Step 5: If there's only one node in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # Step 6: If there are multiple nodes
        else:
            self.tail = self.tail.prev  # Move tail to the previous node
            self.tail.next = None       # The new tail's next is now None
        print(f"Deleted {deleted_data} from the end.")
        return deleted_data

    def display(self):
        # Step 7: Display all nodes from head to end
        current = self.head
        if not current:
            print("List is empty.")
            return

        print("Doubly Linked List (Forward): ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

        # Optional: Display in reverse
        current = self.tail
        if not current: # Redundant check if head is not None, but good for clarity
            return
        print("Doubly Linked List (Backward): ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Step 8: Using the Doubly Linked List
print("\n--- Doubly Linked List Operations ---")
dll = DoublyLinkedList()
dll.display()

dll.insert_end(10)
dll.insert_beginning(5)
dll.insert_end(20)
dll.insert_at_arbitrary_position(15, 3) # Between 10 and 20
dll.insert_at_arbitrary_position(2, 1)  # New head
dll.insert_at_arbitrary_position(25, 6) # New tail
dll.insert_at_arbitrary_position(100, 10) # Out of bounds

dll.display() # Expected: 2 <-> 5 <-> 10 <-> 15 <-> 20 <-> 25 <-> None (forward and backward)

dll.delete_beginning() # Should delete 2
dll.display()

dll.delete_end()       # Should delete 25
dll.display()

dll.delete_end()
dll.delete_beginning()
dll.delete_beginning()
dll.delete_end()
dll.display()

dll.delete_beginning() # Try deleting from empty list
dll.delete_end()       # Try deleting from empty list