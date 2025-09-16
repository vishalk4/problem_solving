def gcd(a,b):
    while b != 0 and a != 0:
        if a>b:
            a = a%b
        else:
            b = b%a
    if a == 0:
        return b
    return a
print(gcd(42,24))

def lcm(a,b):
    return a*b//gcd(a,b)
print(lcm(7,3))