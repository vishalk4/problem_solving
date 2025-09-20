def containsDuplicate(lst):
    s = set()
    for i in lst:
        if i in s:
            return True
        s.add(i)
    return False
print(containsDuplicate([1,2,3,4,5,1]))