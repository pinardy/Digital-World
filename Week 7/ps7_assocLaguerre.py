import numpy as np

def assocLaguerre(p,qmp):
    def Lpoly(x):
        masterlist = [[1,-x+1,x**2-4*x+2,-x**3+9*x**2-18*x+6], \
        [1,-2*x+4,3*x**2-18*x+18,-4*x**3+48*x**2-144*x+96], \
        [2,-6*x+18,12*x**2-96*x+144,-20*x**3+300*x**2-1200*x+1200], \
        [6,-24*x+96,60*x**2-600*x+1200,-120*x**3+2160*x**2-10800*x+14400]]
        ans = masterlist[p][qmp]
        return ans
    return Lpoly
f = assocLaguerre(3,0)
print f(1)    
    
#f = assocLaguerre(0,0)
#print f(1)
#      
#f = assocLaguerre(1,1)
#print f(1)
#
#f = assocLaguerre(2,2)
#print f(1)
#
#f = assocLaguerre(2,2)
#print f(0)