from math import pi
def areaCylinder(radius,length):
    area = float(radius*radius*pi)
    volume = float(area*length)
    return area, volume
