def removeDuplicates(llist):
    """
    Removes duplicate nodes from a sorted singly linked list.

    Given the head of a sorted linked list, this function traverses the list and removes all nodes that have duplicate values,
    ensuring that only the first occurrence of each value remains.

    Args:
        llist: The head node of the sorted singly linked list.

    Returns:
        The head node of the modified linked list with duplicates removed.

    Example:
        Input: 1 -> 1 -> 2 -> 3 -> 3
        Output: 1 -> 2 -> 3
    """
    current = llist
    while current and current.next:
        if current.data == current.next.data:
            # Skip the duplicate
            # If the current node's data is equal to the next node's data,
            # update the next pointer to skip the duplicate node.
            current.next = current.next.next
        else:
            # Only move forward if not duplicate
            current = current.next
    return llist