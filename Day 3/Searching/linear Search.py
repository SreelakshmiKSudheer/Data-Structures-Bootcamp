'''Linear search is a simple algorithm used to find a target element in a list by checking each element one by one
 from the beginning to the end. It continues until the target is found or the list ends. Unlike binary search, 
 linear search does not require the list to be sorted. Though easy to implement, it is less efficient for large datasets.'''

def linear_search(arr, target):
    """
    Performs a linear search on the list 'arr' for the value 'target'.
    Returns the index if found, otherwise returns -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

# Ask the user to enter the list of numbers (space-separated)
user_input = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, user_input.split()))

# Ask the user to enter the number to search for
target = int(input("Enter the number to search for: "))

# Perform the search
result = linear_search(numbers, target)

# Show the result
if result != -1:
    print("Value "+str(target)+" found at index "+str(result)+".")
else:
    print("Value "+str(target)+" not found in the list.")
    
# This code performs a linear search on a list of numbers provided by the user.
# time complexity: O(n)
# space complexity: O(1)