class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnnumber > 0:
            columnnumber -= 1  # make it 0-based
            remainder = columnnumber % 26
            # convert 0-25 to A-Z
            result = chr(ord('A') + remainder) + result
            columnnumber //= 26

        return result
