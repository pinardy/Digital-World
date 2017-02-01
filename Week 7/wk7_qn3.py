import numpy as np
 
def sphericalToCartesian(r,theta,phi):
    x=r*np.sin(phi)*np.cos(theta)
    y=r*np.sin(phi)*np.sin(theta)
    z=r*np.cos(phi)
    
    return round(x,5),round(y,5),round(z,5)
    
#print sphericalToCartesian(3,0,3.14) 
#print sphericalToCartesian(3,3.14,0)
#print sphericalToCartesian(3,3.14,3.14)


def cartesianToSpherical(x, y, z):
    r=(x**2.0+y**2.0+z**2.0)**0.5
    
    phi=np.arccos(z/(x**2+y**2+z**2)**0.5)
    if x==0:
        theta=np.pi/2
    else:
        theta=np.arctan(y/x)
        
    
    return round(r,5), round(phi,5),round(theta,5)
    
#print cartesianToSpherical(3,0,0)
print cartesianToSpherical(0,3,0)
print cartesianToSpherical(0,0,3)