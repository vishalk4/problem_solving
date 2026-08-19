class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n is negative x^(-n) = 1 / x^n
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        # keep reducing n until it becomes 0
        while n > 0:
            # if n is odd multiply result by current x
            if n % 2 == 1:
                result = result * x
            x = x * x
            n = n // 2
        return result
