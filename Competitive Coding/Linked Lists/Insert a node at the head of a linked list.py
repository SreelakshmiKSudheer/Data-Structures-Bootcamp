def insertNodeAtHead(llist, data):
    # Write your code here
    newNode = SinglyLinkedListNode(data)
    
    newNode.next = llist
    
    return newNode