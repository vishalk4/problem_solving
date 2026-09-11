class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # put each positive number at its correct index
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # find the first index where the number is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        # all numbers 1 to n are present
        return n + 1
