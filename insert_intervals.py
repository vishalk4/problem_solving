class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        # add intervals that are completely before newinterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        # merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            # take the smaller start
            newInterval[0] = min(newInterval[0], intervals[i][0])
            # take the larger end
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        # add the new or merged interval
        result.append(newInterval)
        # 3. add all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        return result
