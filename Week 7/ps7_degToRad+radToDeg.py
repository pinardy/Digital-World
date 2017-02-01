import numpy as np

def degToRad(deg):
    rad = np.pi*deg/180
    return round(rad,5)
    
#print degToRad(270)

def radToDeg(rad):
    deg = 180*rad/np.pi
    return round(deg,5)
    
#print radToDeg(3.14)
#print radToDeg(3.14/2.0)
#print radToDeg(3.14*3/4)