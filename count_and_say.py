class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        # start with the first sequence
        result = "1"
        # generate sequence from 2 to n
        for _ in range(2, n + 1):
            # this will store the next sequence
            new_result = ""
            # start reading from the first character
            i = 0
            # process the entire current string
            while i < len(result):
                # store the current character
                current = result[i]
                # count consecutive occurrences
                count = 0
                while i < len(result) and result[i] == current:
                    count += 1
                    i += 1
                # add count + character
                new_result += str(count) + current
            # move to the next sequence
            result = new_result
        return result
