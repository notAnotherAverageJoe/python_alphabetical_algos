# We have an array [1,2,3,4,5,6,7,8,9,10] and a target = 7
# and we want to return the index of the target number


def find(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
print(find(a1, target)) # index 6


# We love the Lord and give Him praise for each day
