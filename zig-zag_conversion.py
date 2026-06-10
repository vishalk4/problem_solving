class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if only one row is given or string length is shorter than no.of rows return original string
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        # Start from the first row
        c = 0
        # True means moving down, False means moving up
        gd = False
        # Traverse each character in the string
        for char in s:
            # Add current character to the correct row
            rows[c] += char
            # If we are at the first row or last row we should change gd value
            if c == 0 or c == numRows - 1:
                gd = not gd
            # Move to next row depending on gd value
            if gd:
                c += 1
            else:
                c -= 1
        return "".join(rows)
