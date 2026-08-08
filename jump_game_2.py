class Solution:
    def jump(self, nums: List[int]) -> int:
        # number of jumps we have taken
        jumps = 0
        # how far we can go with current jump
        c = 0
        # farthest we can reach while exploring current range
        f = 0
        for i in range(len(nums) - 1):
            # update the f we can reach
            f = max(f, i + nums[i])
            # if we reach the end of current jump range
            if i == c:
                jumps += 1 # take a jump
                c = f  # update new range
        return jumps
