def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    fibo = [0,1]
    for i in range(2,n):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo
print(fibonacci(10))