
def rotateLeft(d, arr):
    """
    Rotates the elements of the given array to the left by a specified number of positions.

    Parameters:
        d (int): The number of positions to rotate the array to the left.
        arr (list): The list of elements to be rotated.

    Returns:
        list: A new list with the elements rotated to the left by 'd' positions.

    Example:
        >>> rotateLeft(2, [1, 2, 3, 4, 5])
        [3, 4, 5, 1, 2]
    """
    # Write your code here
    l = len(arr)                                    # Get the length of the input array
    result = [arr[(i + d) % l] for i in range(l)]   # Create a new list by picking elements from the rotated positions
    # result = [arr[(i-l+d)] for i in range(l)]     # Alternative approach (commented out)
    return result                                   # Return the rotated array