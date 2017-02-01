import numpy as np
import math as m

def sphericalToCartesian(r,t,p):
    x = round(r*np.sin(p)*np.cos(t),5)
    y = round(r*np.sin(p)*np.sin(t),5)
    z = round(r*np.cos(p),5)
    return x,y,z
    
#print sphericalToCartesian(3,0,3.14)
#print sphericalToCartesian(3,3.14,0)

def cartesianToSpherical(x,y,z):
    r = np.sqrt(x**2+y**2+z**2)
    if x == 0:
        t = np.pi/2
    else:
        t = np.arctan(y/x)
    p = np.arccos(z/np.sqrt(x**2+y**2+z**2))
    return round(r,5),round(p,5),round(t,5)
    
print cartesianToSpherical(3,0,0)
print cartesianToSpherical(0,3,0)
print cartesianToSpherical(0,0,3)
    