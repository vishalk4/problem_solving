class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0
        star = -1
        match = 0
        while i < len(s):
            # case 1: current characters match directly and '?' can match any single character
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                # Move both pointers forward
                i += 1
                j += 1
            # case 2: we found * initially assume * matches zero characters
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1
            # case 3: current characters don't match and we have not seen a * before
            elif star == -1:
                return False
            # case 4: current characters don't match but we have seen a * before
            else:
                match += 1
                j = star + 1
                i = match
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)
