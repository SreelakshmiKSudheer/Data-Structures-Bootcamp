def deleteNode(llist, position):
    # Write your code here
    if position == 0:
        return llist.next

    count = 0
    ptr = llist

    while count < position - 1 and ptr is not None and ptr.next is not None:
        ptr = ptr.next
        count += 1

    if ptr is not None and ptr.next is not None:
        ptr.next = ptr.next.next

    return llist
