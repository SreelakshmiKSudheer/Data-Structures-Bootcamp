def findMergeNode(head1, head2):
    """
    Finds the data value of the node where two singly linked lists merge.
    Given the heads of two singly linked lists that merge at some point, this function returns
    the data value of the node where the two lists merge. If the lists do not merge, the function
    returns None.
    The function works by first calculating the lengths of both lists, aligning the starting points
    so that both pointers have the same number of nodes to traverse until the end, and then traversing
    both lists in tandem to find the merge point.
    Args:
        head1: The head node of the first singly linked list.
        head2: The head node of the second singly linked list.
    Returns:
        The data value (int) of the merge point node if the lists merge, otherwise None.
    """
    def get_length(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    len1 = get_length(head1)
    len2 = get_length(head2)

    # Align both heads to same starting point from merge
    if len1 > len2:
        for _ in range(len1 - len2):
            head1 = head1.next
    else:
        for _ in range(len2 - len1):
            head2 = head2.next

    # Traverse together until merge point
    while head1 and head2:
        if head1 == head2:
            return head1.data
        head1 = head1.next
        head2 = head2.next