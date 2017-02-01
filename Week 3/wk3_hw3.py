def getEvenNumber(x):
    even = []  
    for n in x:  
        if n % 2 == 0:  
            even.append(n)  
    return even    



print 'getEvenNumber([1,2,3,4,5])'
ans=getEvenNumber([1,2,3,4,5]) 
print ans

print 'getEvenNumber([11,22,33,44,55])'
ans=getEvenNumber([11,22,33,44,55]) 
print ans

print 'getEvenNumber([10,20,30,40,50])'
ans=getEvenNumber([10,20,30,40,50]) 
print ans

print 'getEvenNumber([11,21,31,41,51])'
ans=getEvenNumber([11,21,31,41,51]) 
print ans