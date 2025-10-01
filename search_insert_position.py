def search_insert(nums, target):
    if target in nums:
        return nums.index(target)
    start = 0
    end = len(nums)-1
    mid = 0
    while start <= end:
        mid = (start+end)//2
        if nums[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return mid+1
print(search_insert([1,2,3,5,6,7,8,9], 1))