class Node:
    def __init__(self, data):  # Constructor to initialize the node
        self.data = data        # Store the value/data
        self.next = None        # Initialize next pointer to None (no next node yet)

class SinglyLinkedList:
    def __init__(self):
        self.head = None        # Start with an empty list, so head is None

    def insert_beginning(self, data):
        # Step 3: Create a new node with the given data
        new_node = Node(data)  # Create a node with the provided data

        # Step 4: Link the new node to the current head
        new_node.next = self.head  # The new node's next points to the current head

        # Step 5: Update the head to the new node
        self.head = new_node      # The new node becomes the new head
        print(f"Inserted {data} at the beginning.")

    def insert_end(self, data):
        # Step 3: Create a new node with the given data
        new_node = Node(data)  # Create a node with the provided data

        # Step 4: Check if the list is empty
        if not self.head:      # If head is None, list is empty
            self.head = new_node  # Make new_node the first node (head)
            print(f"Inserted {data} at the end (list was empty).")
            return             # Exit after inserting the first node

        # Step 5: If list is not empty, find the last node
        current = self.head    # Start from the head node
        while current.next:    # Loop until we reach the last node
            current = current.next  # Move to the next node

        current.next = new_node  # Link last node's next to new_node
        print(f"Inserted {data} at the end.")

    def insert_at_arbitrary_position(self, data, position):
        # Step 3: Handle invalid position (less than 1)
        if position < 1:
            print("Position should be 1 or greater.")
            return

        new_node = Node(data) # Create a new node

        # Step 4: If inserting at the beginning (position 1)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            print(f"Inserted {data} at position {position}.")
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

        # Step 7: Insert the new node
        new_node.next = current.next
        current.next = new_node
        print(f"Inserted {data} at position {position}.")

    def delete_beginning(self):
        # Step 3: Check if the list is empty
        if not self.head:
            print("List is empty, cannot delete from the beginning.")
            return None

        # Step 4: Store the data of the node to be deleted
        deleted_data = self.head.data

        # Step 5: Move the head to the next node
        self.head = self.head.next
        print(f"Deleted {deleted_data} from the beginning.")
        return deleted_data

    def delete_arbitrary_position(self, position):
        # check if the list is empty
        if not self.head:
            print("List is empty, cannot delete from arbitrary position.")
            return None

        # if position is 1 (beginning)
        if position == 1:
            deleted_data = self.head.data
            self.head = self.head.next # move the head to next node
            print(f"Deleted {deleted_data} from position {position}.")
            return deleted_data
        
        # traverse to the node right before position 
        current = self.head
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1

        # check if position is out of bounds
        if not current.next:
            print(f"Position {position} is out of bounds. List has fewer than {position-1} elements.")
            return None

        # store data of the required node and delete it
        deleted_data = current.next.data
        deleted_node = current.next
        current.next = current.next.next
        deleted_node = None
        print(f"Deleted {deleted_data} from position {position}.")
        return deleted_data

    def delete_end(self):
        # Step 3: Check if the list is empty
        if not self.head:
            print("List is empty, cannot delete from the end.")
            return None

        # Step 4: If there's only one node in the list
        if not self.head.next:
            deleted_data = self.head.data
            self.head = None  # Make the head None as the list becomes empty
            print(f"Deleted {deleted_data} from the end (only node).")
            return deleted_data

        # Step 5: Traverse to the second to last node
        current = self.head
        while current.next.next:  # Loop until current.next is the last node
            current = current.next

        # Step 6: Store the data of the last node and remove it
        deleted_data = current.next.data
        current.next = None     # Disconnect the last node
        print(f"Deleted {deleted_data} from the end.")
        return deleted_data

    def display(self):
        # Step 6: Display all nodes from head to end
        current = self.head    # Start from the head
        if not current:
            print("List is empty.")
            return

        print("Linked List: ", end="")
        while current:         # Loop until we reach the end (None)
            print(current.data, end=" -> ")  # Print node's data
            current = current.next # Move to the next node
        print("None")          # Print None at the end to indicate end of list

# Step 7: Using the Singly Linked List
print("--- Singly Linked List Operations ---")
sll = SinglyLinkedList()  # Create an empty linked list
sll.display()

sll.insert_end(10)
sll.insert_beginning(5)
sll.insert_end(20)
sll.insert_at_arbitrary_position(15, 3) # Insert 15 at position 3 (between 10 and 20)
sll.insert_at_arbitrary_position(2, 1)  # Insert 2 at position 1 (new head)
sll.insert_at_arbitrary_position(25, 6) # Insert 25 at the end
sll.insert_at_arbitrary_position(100, 10) # Out of bounds

sll.display() # Expected: 2 -> 5 -> 10 -> 15 -> 20 -> 25 -> None

sll.delete_beginning() # Should delete 2
sll.display() # Expected: 5 -> 10 -> 15 -> 20 -> 25 -> None

sll.delete_end()       # Should delete 25
sll.display() # Expected: 5 -> 10 -> 15 -> 20 -> None

sll.delete_end()
sll.delete_beginning()
sll.delete_beginning()
sll.delete_end()
sll.display() # Expected: List is empty.

sll.delete_beginning() # Try deleting from empty list
sll.delete_end()       # Try deleting from empty list
