class Solution:
    def grayCode(self, n: int) -> list[int]:
        # start with Gray Code for 0 bits
        result = [0]
        # generate Gray Code for each bit
        for i in range(n):
            # take the existing numbers in reverse order and add 2^i to each of them
            for num in reversed(result):
                result.append(num + (1 << i))
        return result
