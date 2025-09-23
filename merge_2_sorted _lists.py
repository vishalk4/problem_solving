def merge_lists(l1, l2):
    i = 0
    j = 0
    l3 = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1
    l3.extend(l1[i:])
    l3.extend(l2[j:])
    return l3
print(merge_lists([1,2,3,4,5],[6,7,8,9]))
