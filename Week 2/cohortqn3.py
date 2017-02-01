def posVel(v,t):
    g = 9.81
    y = round(float(v*t - 0.5*g*(t**2)),2)
    y_diff = round(float(v - g*t),2)
    return y, y_diff 

#def posVel(v,t):
#    g = 9.81
#    y = float(v*t - 0.5*g*(t**2))
#    y_diff = float(v - g*t)
#    return y, y_diff 


