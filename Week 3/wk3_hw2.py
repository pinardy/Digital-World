# -*- coding: utf-8 -*-
def tempConvert(type, number):
    
    if type == 'C':
        fahr = float(number)
        cent = float(((fahr-32)*5)/9)
        return cent
    elif type == 'F':
        cent = float(number)
        fahr = float((cent*9)/5 + 32)
        return fahr
    else:
        return None
        
print '''Test case 1: F = 32''' 
ans=tempConvert('F', 32) 
print ans

print '''Test case 2: F = -40''' 
ans=tempConvert('F', -40) 
print ans

print '''Test case 3: F= 212'''
ans=tempConvert('F', 212) 
print ans

print '''Test case 4: C = 0''' 
ans=tempConvert('C', 0) 
print ans

print '''Test case 5: C = -40''' 
ans=tempConvert('C', -40) 
print ans

print '''Test case 6: C = 100'''
ans=tempConvert('C', 100) 
print ans

print '''Test case 7: Neither ’C’ nor ’F'''
ans=tempConvert('', 0) 
print ans

print '''Test case 8: Neither 'C' nor 'F''' 
ans=tempConvert('A', 0) 
print ans
