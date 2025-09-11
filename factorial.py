# method 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
# method 2
def factorial_recursive(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(factorial_recursive(5))
# method 3
import math

print(math.factorial(5))