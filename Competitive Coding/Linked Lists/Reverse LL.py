def reverse(llist):
    # Write your code here
    current = llist
    prev = None
    
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
        