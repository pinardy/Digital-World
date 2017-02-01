from ps7_assocLaguerre import assocLaguerre
from ps7_fact import fact
import numpy as np
import scipy.constants as c
a = c.physical_constants['Bohr radius'][0]
def radial_wave_func(n,l,r):
    p = 2*l+1
    qmp = n-l-1
    #print p,qmp
    lfunc = assocLaguerre(p,qmp)
    a = c.physical_constants['Bohr radius'][0]
    #print lfunc
    y = lfunc(2*r/(n*a))
    #print y
    radsol = np.sqrt((2/(n*a))**3*fact(n-l-1)/(2*n*(fact(n+l))**3))*np.exp(-r/(n*a))*((2*r/(n*a))**l)*y
    ans = radsol/(a**-1.5)
    return np.round(ans,5)
    

print radial_wave_func(1,0,a)
#print radial_wave_func(1,0,a)
#print radial_wave_func(2,1,a)
#print radial_wave_func(2,1,2*a)
#print radial_wave_func(3,1,2*a)
