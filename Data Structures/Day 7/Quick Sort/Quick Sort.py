def quickSort(arr, low, high):
    if low < high:
        pivot = arr[low]
        i = low + 1
        j = high
        while i <= j:
            while i <= high and arr[i] <= pivot:
                i += 1
            while j >= low and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        pi = j
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def main():
    n = int(input("Enter size : "))
    arr = [0]*n
    print("Enter elements:")
    for i in range(n):
        arr[i] = int(input())
    quickSort(arr, 0, n-1)
    print("Sorted :", *arr)

if __name__ == "__main__":
    main()


# def quickSort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[0]
#     left = [x for x in arr[1:] if x <= pivot]
#     right = [x for x in arr[1:] if x > pivot]

#     return quickSort(left) + [pivot] + quickSort(right)