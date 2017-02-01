from ps7_assocLegendre import assocLegendre
from ps7_fact import fact
import numpy as np
import scipy.constants as c

def angular_wave_func(m,l,theta,phi):
    pfunc = assocLegendre(m,l)
    y = pfunc(theta)
    #print y
    angsol = (-1)**m*np.sqrt(((2*l+1)*fact(l-np.abs(m)))/(4*np.pi*fact(l+np.abs(m))))*np.exp(1j*(m*phi))*y
    return np.round(angsol,5)
    
print angular_wave_func(0,0,0,0)
print angular_wave_func(0,1,c.pi,0)
print angular_wave_func(1,1,c.pi/2,c.pi)
print angular_wave_func(0,2,c.pi,0)