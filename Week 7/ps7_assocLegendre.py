import numpy as np

def assocLegendre(m,l):
    def Lpoly(theta):
        x = np.cos(theta)
        masterlist = [[1],[x,np.sqrt(1-x**2)],[0.5*(3*x**2-1),3*x*np.sqrt(1-x**2),3*(1-x**2)],[0.5*(5*x**3-3*x),1.5*(5*x**2-1)*np.sqrt(1-x**2),15*x*(1-x**2),15*(np.sqrt(1-x**2))**3]]
        ans = masterlist[l][m]
        return ans
    return Lpoly
    
#f = assocLegendre(0,0)
#ans = f(1)
#print ans
#
#f = assocLegendre(1,1)
#print f(1)
#
#f = assocLegendre(2,3)
#print f(1)
#
#f = assocLegendre(2,3)
#print f(0)    