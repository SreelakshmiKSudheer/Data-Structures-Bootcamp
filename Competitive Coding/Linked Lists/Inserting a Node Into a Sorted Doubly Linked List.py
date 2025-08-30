def sortedInsert(llist, data):
    """
    Inserts a new node with the given data into a sorted doubly linked list, maintaining the sorted order.
    Args:
        llist (DoublyLinkedListNode): The head node of the sorted doubly linked list.
        data (int): The data value to insert into the list.
    Returns:
        DoublyLinkedListNode: The head node of the updated doubly linked list.
    Behavior:
        - If the list is empty, creates a new node and returns it as the head.
        - If the new data is less than the head's data, inserts the new node at the beginning.
        - Otherwise, traverses the list to find the correct position and inserts the new node,
          updating the previous and next pointers accordingly.
    """
    # Create a new node with the given data
    new_node = DoublyLinkedListNode(data)

    # Case 1: If the list is empty, return the new node as the head
    if not llist:
        return new_node

    # Case 2: If the new data is less than the head's data, insert at the beginning
    if data < llist.data:
        new_node.next = llist      # Point new node's next to current head
        llist.prev = new_node      # Set current head's prev to new node
        return new_node            # New node becomes the new head

    # Case 3: Insert in the middle or end
    current = llist
    # Traverse the list to find the correct position to insert
    while current.next and current.next.data < data:
        current = current.next

    # Insert the new node after 'current'
    new_node.next = current.next  # New node's next points to current's next
    new_node.prev = current       # New node's prev points to current

    # If not inserting at the end, update the next node's prev pointer
    if current.next:
        current.next.prev = new_node

    current.next = new_node       # Current's next points to new node

    return llist                  # Return the (unchanged) head of the list
