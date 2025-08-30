def reverse(llist):
    """
    Reverses a singly linked list.
    Args:
        llist: The head node of the singly linked list to be reversed.
    Returns:
        The new head node of the reversed linked list.
    Example:
        Given a linked list: 1 -> 2 -> 3 -> None
        After calling reverse(llist), the list becomes: 3 -> 2 -> 1 -> None
    """
    # Initialize current node as the head of the list
    current = llist
    # Initialize previous node as None (since the new tail will point to None)
    prev = None 

    # Traverse the linked list
    while current:
        # Store the next node before changing the link
        nxt = current.next
        # Reverse the current node's pointer
        current.next = prev
        # Move prev and current one step forward
        prev = current
        current = nxt
    # prev will be the new head of the reversed list
    return prev
        