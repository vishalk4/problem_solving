class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                # swap elements across the main diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # this gives the matrix rotated 90 degrees clockwise.
        for i in range(n):
            matrix[i].reverse()
        
