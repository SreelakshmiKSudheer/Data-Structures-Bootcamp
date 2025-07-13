# Merge Sort: Divides the array into halves, sorts them, and merges the sorted halves.

def merge_sort(arr):
    if len(arr) > 1:    # Base case: if the array has one or no elements, it's already sorted
        mid = len(arr) // 2  # Find the middle point
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        i, j, k = 0, 0, 0
        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:    # Compare elements from both halves
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]          
                j += 1
            k += 1

        # Copy any remaining elements (only one half will have remaining elements)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [12, 11, 13, 5, 6]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:  ", arr)

# Output:
# Original array: [12, 11, 13, 5, 6]
# Sorted array:  [5, 6, 11, 12, 13]

# Time Complexity: O(n log n) for all cases
# Space Complexity: O(n) for the temporary arrays used during merging


# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr)//2
#     left = mergeSort(arr[:mid])
#     right = mergeSort(arr[mid:])
#     return merge(left, right)

# def merge(left, right):
#     merged = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1
#     merged.extend(left[i:])
#     merged.extend(right[j:])

#     return merged