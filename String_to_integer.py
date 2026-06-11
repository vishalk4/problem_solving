class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        while i < n and s[i] == ' ': # skip leading whitespaces
            i += 1
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):# check if the sign is positive or negative
            if s[i] == '-':
                sign = -1
            i += 1
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        while i < n and s[i].isdigit():
            digit = int(s[i])      # Convert current character to integer
            if result > (INT_MAX - digit) // 10:  # check if the result exeeds INT_MAX before updating result
                return INT_MAX if sign == 1 else INT_MIN # If result is exeeding INT_MAX return INT_MAX
            result = result * 10 + digit # add the digit to the result
            i += 1
        return sign * result
