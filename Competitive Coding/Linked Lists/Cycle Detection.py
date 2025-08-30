def has_cycle(head):
    """
    Detects if a linked list contains a cycle.
    Uses Floyd's Tortoise and Hare algorithm to determine whether a cycle exists in a singly linked list.
    Two pointers, slow and fast, traverse the list at different speeds. If they ever meet, a cycle exists.
    Args:
        head (ListNode): The head node of the singly linked list.
    Returns:
        int: 1 if a cycle is detected in the linked list, 0 otherwise.
    """
    slow = head                  # Initialize slow pointer to head
    fast = head                  # Initialize fast pointer to head

    while fast and fast.next:    # Continue while there are at least two nodes ahead
        slow = slow.next           # Move slow pointer by one node
        fast = fast.next.next      # Move fast pointer by two nodes

        if slow == fast:           # If slow and fast meet, a cycle exists
            return 1               # Return 1 indicating cycle detected

    return 0                       # If loop ends, no cycle found; return 0