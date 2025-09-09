def palindrome(num):
    rev = 0
    store = num
    while num > 0:
        rem = num % 10 #num = 121
        rev = rev *10 + rem
        num = num // 10
    if rev == store:
        return "is a palindrome",rev
    else:
        return "is not a palindrome",rev
print(palindrome(12345))