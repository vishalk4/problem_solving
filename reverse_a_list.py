def reverse_list(lst):
    i = 0
    j = len(lst)-1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return lst
print(reverse_list([1,2,3,4,5]))