class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # base index to calculate length
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(':
                # push index of '('
                stack.append(i)
            else:
                # pop for matching ')'
                stack.pop()

                if not stack:
                    # no base → push current index
                    stack.append(i)
                else:
                    # calculate valid length
                    length = i - stack[-1]
                    max_length = max(max_length, length)
        return max_length
