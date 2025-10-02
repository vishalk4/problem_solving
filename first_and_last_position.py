def left_index(nums, target):
    start = 0
    end = len(nums)-1
    i = -1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] < target:
            start = mid+1
        elif nums[mid] > target:
            end = mid-1
        else:
            i = mid
            end = mid-1
    return i
def right_index(nums, target):
    start = 0
    end = len(nums)-1
    i = -1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] < target:
            start = mid+1
        elif nums[mid] > target:
            end = mid-1
        else:
            i = mid
            start = mid+1
    return i
print([left_index([1,2,3,4,5,5,5],5),right_index([1,2,3,4,5,5,5],5)])