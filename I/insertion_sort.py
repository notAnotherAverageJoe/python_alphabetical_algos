

def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        
        while(j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j-=1
        arr[j+1] = key
        
    return arr

arr1 = [2,5,4,3,7,8,1]
print(insertion_sort(arr1))