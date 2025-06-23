class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0 # Keep track of the number of nodes

    def insert_beginning(self, data):
        # Step 3: Create a new node
        new_node = Node(data)

        # Step 4: If the list is empty
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        # Step 5: If the list is not empty
        else:
            last_node = self.head.prev # The last node is the one before the head
            new_node.next = self.head
            new_node.prev = last_node
            self.head.prev = new_node
            last_node.next = new_node
            self.head = new_node # New node becomes the head
        self.count += 1
        print(f"Inserted {data} at the beginning.")

    def insert_end(self, data):
        # Step 3: Create a new node
        new_node = Node(data)

        # Step 4: If the list is empty
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        # Step 5: If the list is not empty
        else:
            last_node = self.head.prev
            new_node.prev = last_node
            new_node.next = self.head
            last_node.next = new_node
            self.head.prev = new_node
        self.count += 1
        print(f"Inserted {data} at the end.")

    def insert_at_arbitrary_position(self, data, position):
        # Step 3: Handle invalid position
        if position < 1 or (self.count < position -1 and self.head):
            print(f"Position {position} is out of bounds or invalid for current list size ({self.count}).")
            return
        
        new_node = Node(data)

        # Step 4: If inserting at the beginning (position 1)
        if position == 1:
            self.insert_beginning(data)
            return

        # Step 5: If inserting at the end (position is current.count + 1)
        if position == self.count + 1:
            self.insert_end(data)
            return

        # Step 6: Traverse to the node *before* the desired position
        current = self.head
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1

        # Step 7: Check if the position is out of bounds (after traversal)
        if not current or current == self.head.prev: # if current is last node and position is not count+1
             print(f"Position {position} is out of bounds.")
             return

        # Step 8: Insert the new node
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
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
            last_node = self.head.prev
            self.head = self.head.next
            self.head.prev = last_node
            last_node.next = self.head
        self.count -= 1
        print(f"Deleted {deleted_data} from the beginning.")
        return deleted_data

    def delete_end(self):
        # Step 3: Check if the list is empty
        if not self.head:
            print("List is empty, cannot delete from the end.")
            return None

        # Step 4: Store the data of the node to be deleted
        deleted_data = self.head.prev.data

        # Step 5: If there's only one node
        if self.head.next == self.head:
            self.head = None
        # Step 6: If there are multiple nodes
        else:
            second_to_last_node = self.head.prev.prev
            second_to_last_node.next = self.head
            self.head.prev = second_to_last_node
        self.count -= 1
        print(f"Deleted {deleted_data} from the end.")
        return deleted_data

    def display(self):
        # Step 7: Display all nodes
        if not self.head:
            print("List is empty.")
            return

        print("Circular Doubly Linked List (Forward): ", end="")
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print(f" (Head: {self.head.data}, Tail: {self.head.prev.data})") # Indicate head and tail

        # Optional: Display in reverse
        print("Circular Doubly Linked List (Backward): ", end="")
        current = self.head.prev # Start from the tail
        while True:
            print(current.data, end=" <-> ")
            current = current.prev
            if current == self.head.prev: # Stop when we loop back to tail
                break
        print(f" (Head: {self.head.data}, Tail: {self.head.prev.data})")

# Step 8: Using the Circular Doubly Linked List
print("\n--- Circular Doubly Linked List Operations ---")
cdll = CircularDoublyLinkedList()
cdll.display()

cdll.insert_end(10)
cdll.insert_beginning(5)
cdll.insert_end(20)
cdll.insert_at_arbitrary_position(15, 3) # Between 10 and 20
cdll.insert_at_arbitrary_position(2, 1)  # New head
cdll.insert_at_arbitrary_position(25, 6) # New tail (after 20)
cdll.insert_at_arbitrary_position(100, 10) # Out of bounds

cdll.display() # Expected: