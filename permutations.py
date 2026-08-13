class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path, used):
            # if path contains all numbers
            if len(path) == len(nums):
                result.append(path[:])
                return
            # try every number
            for i in range(len(nums)):
                # skip numbers already used
                if used[i]:
                    continue
                # choose
                path.append(nums[i])
                used[i] = True
                backtrack(path, used)
                # undo choice
                path.pop()
                used[i] = False
        backtrack([], [False] * len(nums))
        return result
