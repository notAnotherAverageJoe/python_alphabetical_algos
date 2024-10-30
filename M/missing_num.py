# given an array such as [1,2,3,5,6,7]
# find the missing number


#time complex O(n)
#space complex O(n)

def find_missing_number(arr):
    n = len(arr) + 1
    # this will give the summed number plus the one missing
    expected_sum = n * (n + 1) // 2

    current_num = 0
#   or current_num = sum
    for i in range(len(arr)):
        current_num += arr[i]
    found_missing_number = expected_sum - current_num

    return found_missing_number


a1 = [1, 2, 3, 5, 6, 7]
print(find_missing_number(a1))

# using the built in sum optimized in C so slightly more efficient
def find_missing(arr):
    n = len(arr) + 1
    
    expected_sum = n * (n +1) // 2
    
    curent_num = sum(arr)
    
    found_missing = expected_sum - curent_num
    
    return found_missing


a1 = [1, 2, 3, 5, 6, 7]
print(find_missing(a1))