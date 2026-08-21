class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        # continue until all elements are visited
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            # top row is completed
            # move top boundary down
            top += 1
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            # Right column is completed
            # Move right boundary left
            right -= 1
            if top <= bottom:
                # reverse the bottom row from right to left
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])
                # bottom row is completed
                # move bottom boundary up
                bottom -= 1
            if left <= right:
                # reverse the left column from bottom to top
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                # left column is completed
                # move left boundary right
                left += 1
        return ans
