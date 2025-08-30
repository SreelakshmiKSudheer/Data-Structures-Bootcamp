def compare_lists(llist1, llist2):
    """
    Compares two singly linked lists for equality.
    Args:
        llist1: The head node of the first singly linked list.
        llist2: The head node of the second singly linked list.
    Returns:
        int: 1 if both linked lists are identical (same data and structure), 0 otherwise.
    Line by line comments:
        - while llist1 and llist2:
            # Traverse both lists simultaneously as long as neither is exhausted.
        - if llist1.data != llist2.data:
            # If the current nodes' data differ, the lists are not identical.
        - return 0
            # Return 0 immediately if a mismatch is found.
        - llist1 = llist1.next
            # Move to the next node in both lists.
        - return int(not llist1 and not llist2)
            # After traversal, return 1 if both lists ended together (identical length), else 0.
    """
    while llist1 and llist2:
        # Traverse both lists as long as neither is exhausted.
        if llist1.data != llist2.data:
            # If data at current nodes differ, lists are not identical.
            return 0
        llist1 = llist1.next
        # Move to next node in first list.
        llist2 = llist2.next
        # Move to next node in second list.

    return int(not llist1 and not llist2)
    # Return 1 if both lists ended together (identical length), else 0.