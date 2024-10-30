def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swapping was done in this pass
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break
    return arr



def bubbles(arr):
    n =len(arr)
    for i in range(n):
        swapped =False
        
        for j in range(0,n -i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j +1 ], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
    
a1 = [2,5,4,3,6,7,9,10]
print(bubbles(a1))