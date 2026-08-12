class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, current, total):
            if total == target:
                result.append(current.copy())
                return
            if total > target:
                return
            # try every candidate starting from start
            for i in range(start, len(candidates)):
                # choose the current number
                current.append(candidates[i])
                # call backtrack again
                # i is passed again because we can use the same number multiple times
                backtrack(i,current,total + candidates[i])
                # remove the last number so we can try another possibility
                current.pop()
        backtrack(0, [], 0)
        return result
