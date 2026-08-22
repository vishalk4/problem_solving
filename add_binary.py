class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            # get digit from a if i < 0, treat it as 0
            digit_a = int(a[i]) if i >= 0 else 0
            # get digit from b if j < 0, treat it as 0
            digit_b = int(b[j]) if j >= 0 else 0
            # add both digits and carry
            total = digit_a + digit_b + carry
            # binary digit will be 0 or 1
            result.append(str(total % 2))
            # calculate carry
            carry = total // 2
            # Move to the previous digit
            i -= 1
            j -= 1
        # digits were added from right to left so reverse them before returning
        return ''.join(result[::-1])
