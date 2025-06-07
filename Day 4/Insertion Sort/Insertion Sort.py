# Insertion Sort: Builds a sorted array one element at a time by inserting elements into their correct position.

def insertion_sort(arr):
    # Traverse from the second element to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]    # Current element to insert
        j = i - 1       # Index of the previous element

        # Move elements of arr[0..i-1], that are greater than key, one position ahead
        while j >= 0 and arr[j] > key:      # Check if the current element is greater than the key
            arr[j + 1] = arr[j]             # Shift the larger element to the right
            j -= 1                          # Decrement j to check the next element

        # Insert the key at the correct position
        arr[j + 1] = key

        # Print the array at each pass (for understanding)
        print(f"Step {i}: {arr}")


# Example usage
arr = [12, 11, 13, 5, 6]
print("Original array:", arr)   
insertion_sort(arr)
print("Sorted array:  ", arr)

# Output:
# Original array: [12, 11, 13, 5, 6]
# Step 1: [11, 12, 13, 5, 6]
# Step 2: [11, 12, 13, 5, 6]
# # Step 3: [5, 11, 12, 13, 6]
# Step 4: [5, 6, 11, 12, 13]   
# Sorted array:  [5, 6, 11, 12, 13]