def dynamicArray(n, queries):
    """
    Processes a list of queries on a dynamic array structure and returns the results of specific queries.
    Args:
        n (int): The number of sequences to initialize in the dynamic array.
        queries (List[List[int]]): A list of queries, where each query is a list of three integers:
            - The first integer specifies the type of query (1 or 2).
            - The second and third integers are parameters for the query.
    Query Types:
        1 x y: Append integer y to sequence ((x ^ lastAnswer) % n).
        2 x y: Find the value at index (y % size) in sequence ((x ^ lastAnswer) % n), assign it to lastAnswer, and store lastAnswer in the result.
    Returns:
        List[int]: A list containing the results of all type 2 queries (the values of lastAnswer).
    """
    # Write your code here
    lastAnswer = 0
    arr = [[] for i in range(n)]
    ans = []
    
    for q in queries:
        num,x,y = q[0], q[1], q[2]
        idx = (x^lastAnswer) % n
        if num == 1:
            arr[idx].append(y)
        elif num == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            ans.append(lastAnswer)
            
    return ans