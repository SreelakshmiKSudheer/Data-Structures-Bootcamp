def printLinkedList(head):
    ptr = head
    while ptr:
        print(ptr.data)
        ptr = ptr.next