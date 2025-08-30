def insertNodeAtHead(llist, data):
    """
    Inserts a new node with the given data at the head of a singly linked list.
    Args:
        llist (SinglyLinkedListNode or None): The head node of the linked list. Can be None if the list is empty.
        data (int): The data value to insert in the new node.
    Returns:
        SinglyLinkedListNode: The new head node of the linked list after insertion.
    Example:
        head = insertNodeAtHead(head, 5)
    """
    # Create a new node with the given data
    newNode = SinglyLinkedListNode(data)
    
    # Set the next pointer of the new node to the current head of the list
    newNode.next = llist
    
    # Return the new node as the new head of the list
    return newNode