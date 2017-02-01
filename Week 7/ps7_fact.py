def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        start = 1
        for i in range(1,n+1):
            start *= i
        return start
        
#print fact(3)
#print fact(5)
#print fact(4)
#print fact(1)
            