"""An Armstrong number with n digits is a number such that if each of its digits is
raised to the power of n and added together, the sum equals the number itself"""
def armstrong_number(n):
    sum = 0
    store = n
    while n > 0:
        sum = sum + (n % 10) **len(str(store))
        n = n // 10
    if sum == store:
        print("The number is an Armstrong number")
    else:
        print("The number is not an Armstrong number")
armstrong_number(1000001)