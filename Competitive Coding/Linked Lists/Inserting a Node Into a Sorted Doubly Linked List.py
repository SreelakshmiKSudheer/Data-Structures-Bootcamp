def sortedInsert(llist, data):
    new_node = DoublyLinkedListNode(data)

    # Case 1: Empty list
    if not llist:
        return new_node

    # Case 2: Insert at the beginning
    if data < llist.data:
        new_node.next = llist
        llist.prev = new_node
        return new_node

    # Case 3: Insert in the middle or end
    current = llist
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    new_node.prev = current

    if current.next:
        current.next.prev = new_node

    current.next = new_node

    return llist
