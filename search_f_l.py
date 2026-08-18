class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            # find the middle element
            mid = (left + right) // 2
            # if middle element is the target return its index
            if nums[mid] == target:
                return mid
            # check which half is sorted
            if nums[left] <= nums[mid]:
                # left half is sorted
                if nums[left] <= target < nums[mid]:# check if target lies inside the sorted left half
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right half is sorted
                if nums[mid] < target <= nums[right]:# Check if target lies inside the sorted right half
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
