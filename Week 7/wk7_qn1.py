import scipy.constants as c

def energy_n(n):
    #print c.Rydberg
    ryd_joule = (c.h)*(c.c)*c.Rydberg
    #print ryd_joule
    ryd_eV = ryd_joule/(c.e)
    #print ryd_eV
    energy = round((-1*ryd_eV)/(n**2),5)
    
    return energy
    
print energy_n(1) # -13.60569 
print energy_n(2) # -3.40142
print energy_n(3) # -1.51174


#print c.physical_constants["Planck constant"]