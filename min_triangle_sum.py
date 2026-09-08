class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # start from the second-last row
        for i in range(len(triangle) - 2, -1, -1):
            # visit every element in the current row
            for j in range(len(triangle[i])):
                # choose the smaller value from the two
                triangle[i][j] += min(triangle[i + 1][j],triangle[i + 1][j + 1])
        # The top element now contains
        # the minimum path sum
        return triangle[0][0]
