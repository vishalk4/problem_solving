class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # start with the first row
        row = [1]
        for i in range(rowIndex):
            # add 1 at the beginning and end
            # The inner values are calculated from adjacent values
            row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]
        return row
