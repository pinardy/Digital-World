class Coordinate:
    x=0
    y=0
    
p1 = Coordinate()
p2 = Coordinate()
p3 = Coordinate()

from cohortqn4 import areaTriangle
p1.x = float(raw_input('Enter x coordinate of the first point of a triangle: '))
p1.y = float(raw_input('Enter y coordinate of the first point of a triangle: '))
p2.x = float(raw_input('Enter x coordinate of the second point of a triangle: '))
p2.y = float(raw_input('Enter y coordinate of the second point of a triangle: '))
p3.x = float(raw_input('Enter x coordinate of the third point of a triangle: '))
p3.y = float(raw_input('Enter y coordinate of the third point of a triangle: '))

area=round(areaTriangle(p1,p2,p3),1)
print 'The area of the triangle is: %.1f' %(area)