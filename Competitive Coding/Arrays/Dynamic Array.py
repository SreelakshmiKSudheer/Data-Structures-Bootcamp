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
    lastAnswer = 0                               # Initialize lastAnswer to 0 as per problem statement
    arr = [[] for i in range(n)]                 # Create a list of n empty lists (sequences)
    ans = []                                     # List to store the results of type 2 queries

    for q in queries:                            # Iterate through each query in the queries list
        num, x, y = q[0], q[1], q[2]             # Unpack the query into its components
        idx = (x ^ lastAnswer) % n               # Calculate the index using XOR and modulo operations
        if num == 1:                             # If the query type is 1
            arr[idx].append(y)                   # Append y to the sequence at index idx
        elif num == 2:                           # If the query type is 2
            lastAnswer = arr[idx][y % len(arr[idx])]  # Update lastAnswer with the required element
            ans.append(lastAnswer)               # Store lastAnswer in the results list

    return ans                                   # Return the results of all type 2 queries