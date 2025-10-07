def max_sum_subarray(nums,k):
    temp_sum = sum(nums[0:k])
    max_sum = temp_sum
    for i in range(k,len(nums)):
        temp_sum = temp_sum + nums[i]-nums[i-k]
        max_sum = max(max_sum, temp_sum)
    return max_sum
print(max_sum_subarray([5,2,4,1,3,4,5,9],2))
