class Solution:
    def romanToInt(self, s: str) -> int:
        #create a dictionary to map Romam numbers to integers
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0  # this will store the final result
        # loop through each character in the string
        for i in range(len(s)):
            # get the value of current Roman numeral
            current_value = roman_map[s[i]]
            # check if next value is larger (subtraction case)
            if i + 1 < len(s) and roman_map[s[i + 1]] > current_value:
                total -= current_value  # subtract
            else:
                total += current_value  # add
        return total
