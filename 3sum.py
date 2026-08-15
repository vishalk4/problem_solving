class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            # if the current number is the same as the previous one skip it to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            # left starts immediately after i
            # right starts at the end of the array
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # calculate the sum of the three numbers
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    # if found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    # move both pointers
                    left += 1
                    right -= 1
                    # skip duplicate values on the left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # skip duplicate values on the right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:

                    right -= 1
        return result
