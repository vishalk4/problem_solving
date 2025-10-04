def isbadversion(version):
    return version >= 20
def first_bad_version(n):
    start = 0
    end = n
    while start < end:
        mid = (start + end) // 2
        if isbadversion(mid):
            end = mid
        else:
            start = mid + 1
    return start
print(first_bad_version(23))