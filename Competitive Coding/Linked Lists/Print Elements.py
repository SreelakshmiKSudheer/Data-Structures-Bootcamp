def printLinkedList(head):
    """
    Prints all the elements of a singly linked list starting from the given head node.
    Args:
        head: The head node of the singly linked list. Each node is expected to have 'data' and 'next' attributes.
    Returns:
        None. The function prints each node's data to the standard output.
    """
    # Initialize a pointer to the head of the linked list
    ptr = head
    # Traverse the linked list until the pointer becomes None
    while ptr:
        # Print the data stored in the current node
        print(ptr.data)
        # Move the pointer to the next node in the list
        ptr = ptr.next
