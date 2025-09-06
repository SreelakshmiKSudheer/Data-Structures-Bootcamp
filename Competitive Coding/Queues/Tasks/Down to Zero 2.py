from collections import deque
 
def downToZero(n):
    """
    Computes the minimum number of steps required to reduce a given integer `n` to zero,
    using the following operations at each step:
      1. Decrement the number by 1.
      2. Replace the number with the maximum of any pair of its factors (other than 1 and itself).
    The function uses a breadth-first search (BFS) approach to find the shortest sequence of operations.
    Args:
        n (int): The starting integer to be reduced to zero.
    Returns:
        int: The minimum number of steps required to reduce `n` to zero.
    Example:
        >>> downToZero(4)
        3
        # Steps: 4 -> 2 (factor) -> 1 (decrement) -> 0 (decrement)
    """
    
    visited = [False] * (n+1)
    queue = deque()
    queue.append((n,0))
    visited[n] = True
    
    while queue:
        num, step = queue.popleft()
        
        if num == 0:
            return step
        
        if not visited[num-1]:
            queue.append((num-1, step+1))
            visited[num-1] = True
            
        limit = int(num**0.5) + 1
        for i in range(2, limit):
            if num % i == 0:
                factor = max(num//i, i)
                if not visited[factor]:
                    visited[factor] = True
                    queue.append((factor, step+1))