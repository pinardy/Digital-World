class Coordinate:
	def __init__(self,x1=0,y1=0):
		self.x = x1
		self.y = y1
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getXY(self):
		return self.x, self.y
	def setXY(self,x,y):
		self.x=x
		self.x=y
	def getMagnitude(self):
		magn=(self.x**2+self.y**2)**0.5
		return magn
# self is used to identify which obj you are referring to
	# __str__ converts object to string
	# def __str__(self):
	# 	return "A Coordinate at (%2.f, %2.f)"%(self.x,self.y)

p=Coordinate(3,-1)

print (p.getX(),p.getY())
p.setXY(-1,3)
print p.getXY()
