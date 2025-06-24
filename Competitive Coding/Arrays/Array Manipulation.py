
   
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
#def arrayManipulation(n, queries)
    # Write your code here
    
    # arr = [0] * n                       # Initialize an array of zeros with size n
    
    # for a, b, k in queries:             # Iterate through each query
    #     for i in range(a-1, b):         # For each index in the range [a-1, b-1] (1-based to 0-based)
    #         arr[i] += k                 # # Add k to the current element
    # return max(arr)                     # Return the maximum value in the array after all operations

'''
Why the above method does not work:

- Time Complexity:
    - The naive approach (commented out) iterates through each query.
    - For each query, it updates every element in the specified range.
    - The inner loop runs (b - a + 1) times for each query.
    - This results in a total time complexity of O(m * n) in the worst case,
      where m is the number of queries and n is the size of the array.
    - This approach is very slow for large inputs.

     arr = [0] * n                       ---- constant time(order of 1) c1
    
     for a, b, k in queries:             ---- cost: c2 * n              (since it runs n times)
         for i in range(a-1, b):         ---- cost: c3 * n(inner loop) * n(outer loop)
             arr[i] += k                 ---- cost: c3 * n(inner loop) * n(outer loop)
     return max(arr)                     ---- total cost: c1 + (c2*n) + (c3*n*n) + (c3*n*n)

- Efficient Prefix Sum Approach:
    - Only updates the boundaries of the ranges for each query.
    - Computes the prefix sum in a single pass after all queries.
    - Reduces the time complexity to O(n + m).

    # Efficient Prefix Sum Approach:
    # 1. Instead of updating every element in the range [a, b], we only update the boundaries:
    #    - Add k to arr[a]
    #    - Subtract k from arr[b+1]
    # 2. After all queries, compute the prefix sum of the array.
    #    - The running sum at each index gives the actual value after all operations.
    # 3. The maximum value in the prefix sum array is the answer.
    #
    # Example:
    #   n = 5, queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    #   Initial: [0, 0, 0, 0, 0, 0, 0]
    #   After 1st query: [0, 100, 0, -100, 0, 0, 0]
    #   After 2nd query: [0, 100, 100, -100, 0, 0, -100]
    #   After 3rd query: [0, 100, 100, 0, 0, -100, -100]
    #   Prefix sum:      [0, 100, 200, 200, 200, 100, 0]
    #   Max value: 200
'''

def arrayManipulation(n, queries):    
    arr = [0] * (n + 2)  # Initialize an array of zeros with size n+2 (extra space for boundary handling)
    
    for a, b, k in queries:  # Iterate through each query
        arr[a] += k          # Add k at the start index of the range
        arr[b + 1] -= k      # Subtract k just after the end index of the range
    
    max_value = temp = 0     # Initialize variables to track the running sum and maximum value
    for val in arr:          # Iterate through the array to compute prefix sums
        temp += val          # Update the running sum
        if temp > max_value: # If the running sum is greater than the current max, update max_value
            max_value = temp
    
    return max_value         # Return the maximum value found