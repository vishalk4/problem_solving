class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV", "I"]
        result = ""
        # loop through each value-symbol pair
        for i in range(len(values)): 
            # while the current number is greater than or equal to the value
            while num >= values[i]:   
                # append the corresponding Roman symbol to result
                result += symbols[i] 
                # subtract the value from num
                num -= values[i]
                # continue until num becomes smaller than values[i]
        return result
