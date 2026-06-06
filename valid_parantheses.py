class Solution:
    def isValid(self, s: str) -> bool:
        s = []
        # we use dictionary to map closing brackets to their corresponding opening brackets
        mapping = {')': '(','}': '{',']': '['}
        for char in s:
            if char in mapping: # Check if the character is a closing bracket
                if stack:
                    top = stack.pop()   # Pop the top element from s if not empty
                else:
                    top = '#'           # If s is empty, assign a dummy value '#'
                # Check if the popped element matches the expected opening bracket
                if mapping[char] != top:
                    return False 
            else:
                s.append(char) # If it's an opening bracket, push it onto the s
        # After completing all characters If s is empty all brackets matched correctly else some opening brackets were not closed
        return not s
