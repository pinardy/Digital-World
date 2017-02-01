class Triangle:
    def __init__(self,color='green',filled=True,side1=1.0,side2=1.0,side3=1.0):
    	self.color=color
    	self.filled=filled
    	self.side1=side1
    	self.side2=side2
    	self.side3=side3
    def getColor(self):
    	return self.color
    def setColor(self,color):
    	self.color=color
    def getSide1(self):
    	return self.side1
    def getSide2(self):
    	return self.side2
    def getSide3(self):
    	return self.side3
    def getPerimeter(self):
        self.perimeter=self.side1+self.side2+self.side3
        return self.perimeter

t=Triangle()
ans=(t.getColor(),t.getSide1(),t.getSide2(),t.getSide3())
print ans

# t=Triangle('red',False,4.0,3.0,5.0)
# ans=(t.getColor(),t.filled,t.getSide1(),t.getSide2(),t.getSide3())
# print ans

# t=Triangle(side1=4.0,side2=3.0,side3=5.0)
# ans=t.getPerimeter()
# print ans