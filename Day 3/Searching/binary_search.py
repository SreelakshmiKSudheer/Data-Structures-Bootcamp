'''Binary search is an efficient algorithm used to find the position of a target element in a sorted list. 
It works by repeatedly dividing the search range in half, comparing the target to the middle element. 
If the target equals the middle element, it is found. If not, the search continues in the half where the target could exist. 
This method significantly reduces the number of comparisons, making binary search much faster than linear search, 
especially for large datasets.'''

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Midpoint

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search in right half
        else:
            right = mid - 1  # Search in left half

    return -1  # Target not found


# Ask the user to enter the list of numbers (space-separated)
user_input = input("Enter sorted numbers separated by spaces: ")
# Convert the user input into a list of integers
user_list = list(map(int, user_input.split()))
# Ask the user for the target number
target = int(input("Enter the number to search for: "))
# Perform binary search
result = binary_search(user_list, target)
# Display the result
if result != -1:
    print(f"Number found at index: {result}")
else:
    print("Number not found.")

# This code performs a binary search on a sorted list of numbers provided by the user.
# Time complexity: O(log n)
# Space complexity: O(1)
# Note: The input list must be sorted for binary search to work correctly.