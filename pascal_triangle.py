from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = []
            # each row has i + 1 elements
            for j in range(i + 1):
                # first and last elements are always 1
                if j == 0 or j == i:
                    row.append(1)
                # other elements are the sum of two elements from the previous row
                else:
                    row.append(result[i - 1][j - 1] + result[i - 1][j])
            # add the completed row to the result
            result.append(row)
        return result
