class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = [0] * n
        left = 0
        right = n - 1
        # fill result from right to left
        for i in range(n - 1, -1, -1):
            # check for the max negative value
            # and add to the end of the array
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            # else add max positive value 
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result
