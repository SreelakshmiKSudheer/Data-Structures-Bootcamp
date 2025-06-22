# Selection Sort: A simple, comparison-based sorting algorithm.
# It works by dividing the array into a sorted and unsorted part.
# It repeatedly selects the smallest element from the unsorted part
# and moves it to the end of the sorted part.

def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Assume the current index i holds the minimum value
        min_idx = i

        # Find the index of the minimum element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update min_idx if a smaller element is found

        # Swap only if a new minimum was found
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            # Swap the found minimum element with the first element of the unsorted part 

# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:", arr)  # Output: Sorted array is: [11, 12, 22, 25, 64]
# Time Complexity: O(n^2) in the worst and average case bescause of the nested loops
# and O(n) in the best case when the array is already sorted.
# Space Complexity: O(1) as it sorts the array in place
