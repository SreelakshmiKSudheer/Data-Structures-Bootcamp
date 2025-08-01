def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next           # Move 1 step
        fast = fast.next.next      # Move 2 steps

        if slow == fast:
            return 1            # Cycle detected

    return 0                   # No cycle