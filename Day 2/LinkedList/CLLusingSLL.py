class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None  # Head of the list
        self.count = 0    # Keep track of the number of nodes for size-related checks

    def insert_beginning(self, data):
        # Step 3: Create a new node
        new_node = Node(data)

        # Step 4: If the list is empty
        if not self.head:
            self.head = new_node
            new_node.next = self.head # Points to itself to form a circle
        # Step 5: If the list is not empty
        else:
            current = self.head
            while current.next != self.head: # Find the last node
                current = current.next
            new_node.next = self.head        # New node points to the old head
            current.next = new_node          # Last node points to the new node
            self.head = new_node             # New node becomes the head
        self.count += 1
        print(f"Inserted {data} at the beginning.")

    def insert_end(self, data):
        # Step 3: Create a new node
        new_node = Node(data)

        # Step 4: If the list is empty
        if not self.head:
            self.head = new_node
            new_node.next = self.head # Points to itself
        # Step 5: If the list is not empty
        else:
            current = self.head
            while current.next != self.head: # Find the last node
                current = current.next
            current.next = new_node          # Last node points to new node
            new_node.next = self.head        # New node points back to head
        self.count += 1
        print(f"Inserted {data} at the end.")

    def insert_at_arbitrary_position(self, data, position):
        # Step 3: Handle invalid position
        if position < 1 or (self.count < position -1 and self.head): # allow inserting at count + 1 if list is not empty
            print(f"Position {position} is out of bounds or invalid for current list size ({self.count}).")
            return
        
        new_node = Node(data)

        # Step 4: If inserting at the beginning (position 1)
        if position == 1:
            self.insert_beginning(data)
            return

        # Step 5: Traverse to the node *before* the desired position
        current = self.head
        count = 1
        while current.next != self.head and count < position - 1:
            current = current.next
            count += 1

        # Step 6: If inserting at the end (position is current.count + 1)
        if count == position - 1 and current.next == self.head:
            self.insert_end(data)
            return
        
        # Step 7: Insert the new node
        new_node.next = current.next
        current.next = new_node
        self.count += 1
        print(f"Inserted {data} at position {position}.")


    def delete_beginning(self):
        # Step 3: Check if the list is empty
        if not self.head:
            print("List is empty, cannot delete from the beginning.")
            return None

        # Step 4: Store the data of the node to be deleted
        deleted_data = self.head.data

        # Step 5: If there's only one node
        if self.head.next == self.head:
            self.head = None
        # Step 6: If there are multiple nodes
        else:
            current = self.head
            while current.next != self.head: # Find the last node
                current = current.next
            self.head = self.head.next      # Move head to the next node
            current.next = self.head         # Last node points to the new head
        self.count -= 1
        print(f"Deleted {deleted_data} from the beginning.")
        return deleted_data

    def delete_end(self):
        # Step 3: Check if the list is empty
        if not self.head:
            print("List is empty, cannot delete from the end.")
            return None

        # Step 4: Store the data of the node to be deleted
        deleted_data = None

        # Step 5: If there's only one node
        if self.head.next == self.head:
            deleted_data = self.head.data
            self.head = None
        # Step 6: If there are multiple nodes
        else:
            current = self.head
            prev = None
            while current.next != self.head: # Find the last node and its previous
                prev = current
                current = current.next
            deleted_data = current.data
            prev.next = self.head           # Second to last node points to head
        self.count -= 1
        print(f"Deleted {deleted_data} from the end.")
        return deleted_data

    def display(self):
        # Step 7: Display all nodes
        if not self.head:
            print("List is empty.")
            return

        print("Circular Singly Linked List: ", end="")
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head: # Stop when we loop back to head
                break
        print(f" (Head: {self.head.data})") # Indicate the head of the circle

# Step 8: Using the Circular Singly Linked List
print("\n--- Circular Singly Linked List Operations ---")
csll = CircularSinglyLinkedList()
csll.display()

csll.insert_end(10)
csll.insert_beginning(5)
csll.insert_end(20)
csll.insert_at_arbitrary_position(15, 3) # Between 10 and 20
csll.insert_at_arbitrary_position(2, 1)  # New head
csll.insert_at_arbitrary_position(25, 6) # New tail (after 20)
csll.insert_at_arbitrary_position(100, 10) # Out of bounds

csll.display() # Expected: 2 -> 5 -> 10 -> 15 -> 20 -> 25 -> (Head: 2)

csll.delete_beginning() # Should delete 2
csll.display() # Expected: 5 -> 10 -> 15 -> 20 -> 25 -> (Head: 5)

csll.delete_end()       # Should delete 25
csll.display() # Expected: 5 -> 10 -> 15 -> 20 -> (Head: 5)

csll.delete_end()
csll.delete_beginning()
csll.delete_beginning()
csll.delete_end()
csll.display() # Expected: List is empty.

csll.delete_beginning() # Try deleting from empty list
csll.delete_end()       # Try deleting from empty list