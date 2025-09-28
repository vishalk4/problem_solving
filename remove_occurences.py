def remove_occurences(lst,value):
    i = 0
    for j in range(len(lst)):
        if lst[j] != value:
            lst[i] = lst[j]
            i += 1
    del lst[i:]
    return lst
print(remove_occurences([1,2,3,4,5,6,1,1,2,1,3,],1))

