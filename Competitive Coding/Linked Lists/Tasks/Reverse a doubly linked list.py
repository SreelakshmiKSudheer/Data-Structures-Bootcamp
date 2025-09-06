def reverse(llist):
    """
    Reverses a doubly linked list in place.
    Args:
        llist: The head node of the doubly linked list to be reversed.
    Returns:
        The new head node of the reversed doubly linked list.
    Notes:
        - The function assumes that each node in the list has 'next' and 'prev' attributes.
        - The reversal is performed in place, modifying the original list.
    """
    current = llist                     # Start with the head of the list
    new_head = None                     # This will eventually point to the new head after reversal

    while current:                      # Traverse the list until the end
        # Swap next and prev pointers for the current node
        current.prev, current.next = current.next, current.prev
        # Update new_head to the current node (last node processed will be the new head)
        new_head = current
        # Move to the next node in the original list (which is prev after swapping)
        current = current.prev

    return new_head                     # Return the new head of the reversed list