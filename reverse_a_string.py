def reverse(string):
    rev_string = ''
    i = len(string)-1
    while i >= 0:
        rev_string = rev_string + string[i]
        i = i-1
    return rev_string
print(reverse("hello"))