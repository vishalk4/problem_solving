def sqrt_binary(x):
    if x < 0:
        return "square root cannot be negative"
    if x == 0 or x == 1:
        return x
    start = 0
    end = x
    fa = 0
    while start <= end:
        mid = (start + end) // 2
        if mid*mid == x:
            return mid
        elif mid*mid < x:
            fa = mid
            start = mid + 1
        else:
            end = mid - 1
    return fa
print(sqrt_binary(23))
