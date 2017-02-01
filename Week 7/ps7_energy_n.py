import scipy.constants as c
from scipy import constants

def energy_n(n):
    R = constants.physical_constants["Rydberg constant times hc in eV"]
    E = -R[0]*n**(-2)
    return round(E,5)
    
#print energy_n(2)