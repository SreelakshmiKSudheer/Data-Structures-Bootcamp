def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    
    if not head:
        return new_node

    current = head
    while current.next:
        current = current.next
    current.next = new_node
    
    return head