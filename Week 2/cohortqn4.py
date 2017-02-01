from math import sqrt

class Coordinate:
    x=0
    y=0
p1 = Coordinate()
p1.x =1.5
p1.y = -3.4
p2 = Coordinate()
p2.x =4.6
p2.y =5
p3 = Coordinate()
p3.x =9.5
p3.y = -3.4

####################
def areaTriangle(p1,p2,p3):
    side1= sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)
    side2= sqrt((p2.x-p3.x)**2+(p2.y-p3.y)**2)
    side3= sqrt((p3.x-p1.x)**2+(p3.y-p1.y)**2)
    s= (side1+side2+side3)/2
    area= sqrt(s*(s-side1)*(s-side2)*(s-side3))
    
    return area
print round(areaTriangle(p1,p2,p3),1)
####################