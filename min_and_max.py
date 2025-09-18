def min_and_max(lis):
    i = lis[0]
    j = lis[0]
    for x in lis:
        if i > x:
            i = x
        if j < x:
            j = x
    return i,j
print(min_and_max([12,34,2,34,123,230,9]))