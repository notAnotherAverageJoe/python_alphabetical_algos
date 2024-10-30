# we recieve an array [2,3,4,5,7,8,9,10] target of 18
# which two numbers added together will hit the target

#first solution is nested loops O(n^2) but a space compex of O(1)

def two_sum_quadratic(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
               return [i,j]
    return -1

a1 = [2,3,4,5,7,8,9,10]
targ = 18
print(two_sum_quadratic(a1,targ)) #[5,7]


#this is a O(n) solution and a space complexity of O(n)
def two_sum(arr,target):
    count = {}
    for i in range(len(arr)):
        needed_val = target - arr[i]
        if needed_val in count:
            return[count[needed_val], i]
        
        count[arr[i]] = i
    
    return -1
        


a1 = [2,3,4,5,7,8,9,10]
targ = 18
print(two_sum(a1,targ)) #[5,7]
                
