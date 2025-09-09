def find_largest_of_three(a,b,c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    elif c > a and c > b:
        return c

print(find_largest_of_three(2,3,4))
