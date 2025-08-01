def findMergeNode(head1, head2):
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