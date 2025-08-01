def poisonousPlants(p):
    """
    Determines the number of days after which no plants die due to being poisonous.
    In a row of plants, each plant has a pesticide amount. On each day, any plant with more pesticide than the plant to its left dies. 
    The process repeats until no plants die in a day. This function calculates the total number of days until this happens.
    Args:
        p (List[int]): A list of integers representing the pesticide amount for each plant.
    Returns:
        int: The number of days after which no plants die.
    Example:
        >>> poisonousPlants([6, 5, 8, 4, 7, 10, 9])
        2
    """
    # Write your code here
    # stack = []
    # count = 0
    # change = True
    
    # while change:
    #     for i in range(1, len(p)):
    #         if p[i] > p[i-1]:
    #             stack.append(i)
    #     if stack:
    #         change = True
    #         count += 1
    #         while stack:
    #             index = stack.pop()
    #             p.pop(index)
    #     else:
    #         change = False       
                
    # return count
    
    '''
    count = 0
    change = True
    
    while change:
        change = False 
        last = len(p) - 1
        
        for i in range(last, 0, -1):
            if p[i] > p[i-1]:
                p.pop(i)
                change = True
        if change:
            count += 1
    return count
    '''

    # stack = []
    # max_days = 0

    # for i in range(len(p)):
    #     days = 0
        
    #     while stack and p[i] <= p[stack[-1][0]]:
    #         days = max(days, stack[-1][1])
    #         stack.pop()

    #     if not stack:
    #         days = 0
    #     else:
    #         days += 1

    #     max_days = max(max_days, days)
    #     stack.append((i, days))

    # return max_days
    
    stack = []  # Stack to keep track of indices of plants
    days = [0] * len(p)  # Array to store the days each plant will die
    max_days = 0  # Variable to keep track of the maximum days

    for i in range(len(p)):
        d = 0  # Initialize the days for the current plant
        # Remove plants from the stack that have more or equal pesticide than current
        while stack and p[i] <= p[stack[-1]]:
            # Update d to the maximum days among popped plants
            d = max(d, days[stack.pop()])
        if stack:
            # If stack is not empty, current plant will die one day after the last popped plant
            days[i] = d + 1
        # Push current plant index onto the stack
        stack.append(i)
        # Update the maximum days
        max_days = max(max_days, days[i])

    return max_days