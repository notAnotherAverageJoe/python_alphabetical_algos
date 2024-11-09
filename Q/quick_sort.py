def partition(arr, low, high):
    # Choose the pivot (commonly the last element)
    pivot = arr[high]
    i = low - 1  # Pointer for the smaller element

    # Partition the array based on the pivot
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Place the pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the partitioning index

def quicksort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort the subarrays
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

arr = [10, 7, 8, 9, 1, 5]
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)




def quick_sort(arr):
    if len(arr) <=1:
        return arr
    left = []
    right = []
    mid = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < mid:
            left.append(arr[i])
        else:
            right.append(arr[i])
            
    return quick_sort(left) + [mid] + quick_sort(right)

arr1 = [2,5,4,3,7,8,1]
print(quick_sort(arr1))

def quick_sort2(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[0]
    
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    return quick_sort2(left) + [pivot] + quick_sort2(right)

print(quick_sort2(arr1))
