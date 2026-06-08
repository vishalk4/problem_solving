class Solution:
    def reverse(self, x: int) -> int:
        imax = 2**31 - 1 
        imin = -2**31
        s = -1 if x < 0 else 1 # checking that if integer is neagtive or positive
        x = abs(x) # converting integer to positive
        rev = 0
        while x: # iterating through the loop untill integer will be zero
            digit = x % 10 # obtaing the last digit 0f integer by dividing it by 10
            x //= 10 # removing the last digit from integer by dividing
            rev = rev * 10 + digit # append digit to reversed number
        rev *= s #assigning its sign to it
        if rev < imin or rev > imax: # checking if it exeeds the limits
            return 0
        return rev
