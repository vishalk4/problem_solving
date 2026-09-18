class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # make it 0-based
            remainder = columnNumber % 26
            # Convert 0-25 to A-Z
            result = chr(ord('A') + remainder) + result
            columnNumber //= 26

        return result
