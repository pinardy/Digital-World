import scipy.constants as c

def degToRad(deg):
    rad=deg*(c.pi/180)
    return round(rad,5)


def radToDeg(rad):
    deg=rad*(180/c.pi)
    return round(deg,5)
    
print degToRad(90)
