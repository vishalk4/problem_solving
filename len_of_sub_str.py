class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        for i in range(len(s)):
            # if current character is already in the window we have a duplicate.
            while s[i] in seen:
                # remove the character at the left side and move the left pointer forward
                seen.remove(s[left])
                left += 1
            # add the current character to the window
            seen.add(s[i])
            current_len = i - left + 1
            # update maximum length
            max_len = max(max_len, current_len)
        return max_len
