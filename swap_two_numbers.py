def swaptwonumbers(a,b): #a =1,b=2
    a = a+b #a = 1+2=3
    b = a-b #b = 3-2=1
    a = a-b #a = 3-1=2
    return a,b
print(swaptwonumbers(-23,34))