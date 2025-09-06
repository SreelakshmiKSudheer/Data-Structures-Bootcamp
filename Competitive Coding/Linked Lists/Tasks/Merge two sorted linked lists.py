def mergeLists(head1, head2):
    """
    Merges two sorted singly linked lists into a single sorted linked list.
    This function merges the two input linked lists by rearranging the existing nodes,
    resulting in a merged list that maintains the sorted order. The original lists
    are not preserved after the operation (i.e., nodes are reused).
    Args:
        head1 (SinglyLinkedListNode): The head node of the first sorted linked list.
        head2 (SinglyLinkedListNode): The head node of the second sorted linked list.
    Returns:
        SinglyLinkedListNode: The head node of the merged sorted linked list.
    Note:
        - The function operates in O(1) additional space, as it does not create new nodes.
        - If you need to preserve the original lists, consider making deep copies of the nodes.
    """
    # does not maintain the original two lists, Space complexity = O(1)
    dummy = tail = SinglyLinkedListNode(0)

    while head1 and head2:
        if head1.data < head2.data:
            # Attach the current node from the first list to the merged list
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    tail.next = head1 or head2

    return dummy.next
    
    # maintains original lists, but with a Space complexity of O(m+n)
    # not preferred for coding interviews due to increased space complexity, use only if specifically mentioned to maintain the original lists
    
    # dummy = tail = SinglyLinkedListNode(0)

    # while head1 and head2:
    #     if head1.data < head2.data:
    #         tail.next = SinglyLinkedListNode(head1.data)
    #         head1 = head1.next
    #     else:
    #         tail.next = SinglyLinkedListNode(head2.data)
    #         head2 = head2.next
    #     tail = tail.next

    # while head1:
    #     tail.next = SinglyLinkedListNode(head1.data)
    #     head1 = head1.next
    #     tail = tail.next

    # while head2:
    #     tail.next = SinglyLinkedListNode(head2.data)
    #     head2 = head2.next
    #     tail = tail.next

    # return dummy.next
