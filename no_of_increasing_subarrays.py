def no_of_increasing_subarrays(nums):
    x = 0
    y = 0
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            x = x + 1
            y = y + x
        else:
            x = 0
    return y
print(no_of_increasing_subarrays([5,2,4,1,3,4]))
