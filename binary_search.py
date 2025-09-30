def binary_search(nums, target):
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return -1
print(binary_search([1,2,3,5,6,7,8,9], 0))