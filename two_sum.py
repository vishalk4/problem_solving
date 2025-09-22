def two_sum(nums, target):
    d = {}
    for i,b in enumerate(nums):
        a = target-b
        if a in d:
            return d[a],i
        d[b] = i
    return None
print(two_sum([2,7,11,15],9))