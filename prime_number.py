
def prime_number(n):
    if n == 1:
        return "neither prime nor composite"
    for i in range(2, int((n**0.5)) + 1):
        if n % i == 0:
            return "composite number"
    return "prime number"
print(prime_number(23))