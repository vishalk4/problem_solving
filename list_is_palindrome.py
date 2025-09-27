def liat_is_palindrome(lst):
    i = 0
    j = len(lst)-1
    while i < j:
        if lst[i] == lst[j]:
            i+=1
            j-=1
        else:
            return "the list is not palindrome"
    return "the list is palindrome"
print(liat_is_palindrome([1,2,0,2,1]))