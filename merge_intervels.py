class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals based on the starting value
        intervals.sort()
        # store the merged intervals
        result = []
        for start, end in intervals:
            # If result is empty or there is no overlap
            if not result or start > result[-1][1]:
                # add the current interval
                result.append([start, end])
            else:
                # if interval is overlapping 
                result[-1][1] = max(result[-1][1], end)
        return result
