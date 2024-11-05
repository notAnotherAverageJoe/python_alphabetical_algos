# moving all negatives to the front of the array
# and all positives to the back of the array

def yin_yang_sort(arr):
    yin_nums = 0
    
    for i in range(len(arr)):
        if arr[i] < 0:
            if i != yin_nums:
                [arr[i], arr[yin_nums]] = [arr[yin_nums],arr[i]]
            yin_nums+=1
            
    return arr

arr1 =[ -2, -5, -1, -3, 3, 6, 4 ]
print(yin_yang_sort(arr1))

        
        