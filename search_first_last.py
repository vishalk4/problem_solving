class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # function to find the first occurrence of target
        def find_first():
            left = 0
            right = len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    # store the position and continue searching
                    first = mid
                    right = mid - 1
                elif nums[mid] < target:
                    # target is on the right side.
                    left = mid + 1
                else:
                    # target is on the left side.
                    right = mid - 1
            return first
        # function to find the last occurrence of target
        def find_last():
            left = 0
            right = len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    # store the position and continue searching
                    last = mid
                    left = mid + 1
                elif nums[mid] < target:
                    # target is on the right side.
                    left = mid + 1
                else:
                    # target is on the left side.
                    right = mid - 1
            return last
        first = find_first()
        last = find_last()
        return [first, last]
