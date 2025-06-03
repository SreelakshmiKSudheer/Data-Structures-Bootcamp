# Bubble Sort: A simple sorting algorithm that repeatedly steps through the list,
# compares adjacent elements, and swaps them if they are in the wrong order.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted, so we don't need to compare them
        # We loop only up to n - i - 1 to avoid going out of bounds when accessing arr[j + 1]
        for j in range(n - i - 1):
            # Swap if current element is greater than next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)  
# Output: Sorted array is: [11, 12, 22, 25, 34, 64, 90]
# Time Complexity: O(n^2) in the worst and average case, O(n) in the best case (when the array is already sorted)
# Space Complexity: O(1) since it sorts the array in place 
