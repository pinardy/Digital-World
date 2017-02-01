from math import exp

def approx_ode():
    h = 0.1
    t = raw_input('What is your value for t?: ')
    dydt = 3 + exp(-t) - 0.5y
    
    