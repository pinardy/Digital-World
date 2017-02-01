# -*- coding: utf-8 -*-
def check2(n1,n2,n3,x):
    if x > n1 and x > n2 and x < n3:
        return True
    else:
        return False
        
print '''Test case 1: check2(1,4,8,7)''' 
print '''ans = True''' 
ans=check2(1,4,8,7) 
print ans

print '''Test case 2: check2(10,4,8,7)''' 
print '''ans = False''' 
ans=check2(10,4,8,7) 
print ans

print '''Test case 3: check2(1,10,8,7)''' 
print '''ans = False''' 
ans=check2(1,10,8,7) 
print ans

print '''Test case 4: check2(1,4,5,7)''' 
print '''ans = False''' 
ans=check2(1,4,5,7) 
print ans
