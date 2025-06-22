def arrayManipulation(n, queries):
    """
    Performs a series of range update operations on an initially zeroed array and returns the maximum value after all operations.
    Args:
        n (int): The size of the array.
        queries (List[List[int]]): A list of queries, where each query is a list of three integers [a, b, k].
            - a (int): Starting index of the range (1-based, inclusive).
            - b (int): Ending index of the range (1-based, inclusive).
            - k (int): The value to add to each element in the range [a, b].
    Returns:
        int: The maximum value in the array after performing all the queries.
    Note:
        This function uses a prefix sum approach for efficient range updates.
    """
    # Write your code here
    # arr = [0] * n
    # for a,b,k in queries:
    #     for i in range(a-1,b):
    #         arr[i] += k
        
    # return max(arr)
    
    arr = [0] * (n + 2) 
    
    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k
    
    max_value = temp = 0
    for val in arr:
        temp += val
        if temp > max_value:
            max_value = temp
    
    return max_value