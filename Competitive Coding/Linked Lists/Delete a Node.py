def deleteNode(llist, position):
    """
    Deletes the node at the specified position in a singly linked list.
    Args:
        llist (Node): The head node of the singly linked list.
        position (int): The zero-based index of the node to delete.
    Returns:
        Node: The head node of the modified linked list after deletion.
    Notes:
        - If position is 0, the head node is removed and the next node becomes the new head.
        - If position is out of bounds (greater than the length of the list), the list remains unchanged.
        - Assumes the linked list nodes have a 'next' attribute.
    """
    # If the position to delete is 0, remove the head node by returning the next node
    if position == 0:
        return llist.next

    # Initialize a counter and a pointer to traverse the list
    count = 0
    ptr = llist

    # Traverse the list to reach the node just before the one to delete
    while count < position - 1 and ptr is not None and ptr.next is not None:
        ptr = ptr.next
        count += 1

    # If the next node exists, bypass it to delete it from the list
    if ptr is not None and ptr.next is not None:
        ptr.next = ptr.next.next

    # Return the (possibly unchanged) head of the list
    return llist
