class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # create 3 lists of sets to track same numbers
        rows = [set() for _ in range(9)]   # track numbers in each row
        cols = [set() for _ in range(9)]   # track numbers in each column
        boxes = [set() for _ in range(9)]  # track numbers in each 3x3 box
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                # skip empty cells
                if val == '.':
                    continue
                box_index = (i // 3) * 3 + (j // 3)
                # check if value already exists in row, column, or box
                if val in rows[i]:
                    return False
                if val in cols[j]:
                    return False
                if val in boxes[box_index]:
                    return False
                # If not present, add value to the sets
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)
        # if no duplicates found, Sudoku is valid
        return True
