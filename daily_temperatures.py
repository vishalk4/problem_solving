class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from typing import List
        n = len(temperatures)
        # initialize result list with 0s
        ans = [0] * n # default is 0 because if no warmer day exists, answer stays 0
        stack = [] #sStack will store indices of temperatures
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]: # check if current temperature is greater than
                prev_index = stack.pop() # pop the previous index
                ans[prev_index] = i - prev_index # calculate number of days waited
            stack.append(i)  # push current index into stack
        return ans
