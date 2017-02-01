def isPrime(x):
    if x==2:
        return True
    elif x<2 or x % 2 == 0:
        return False
    elif x==2:
        return True
    else:
        return all(x % i for i in xrange(2, x))

#all function: Return True if all elements of the iterable are true 
#(or if the iterable is empty).

#range returns a Python list object and xrange returns an xrange object.
        
        
print 'isPrime(2)' 
ans=isPrime(2) 
print ans

print 'isPrime(3)' 
ans=isPrime(3) 
print ans

print 'isPrime(7)' 
ans=isPrime(7) 
print ans

print 'isPrime(9)' 
ans=isPrime(9) 
print ans

print 'isPrime(21)' 
ans=isPrime(21) 
print ans

