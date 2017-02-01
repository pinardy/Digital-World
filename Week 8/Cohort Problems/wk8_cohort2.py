class Square:
  def __init__(self,x=0):
    self.x=x
  def getArea(self):
    return float(self.x)**2.0
  def setArea(self,area):
    self.x=area**0.5
  def __str__(self):
    return 'Square of height and width %s'%self.x +'.'
s=Square(6)
# print s.getArea()
s.setArea(100)
s1=Square(10)
print s1.getArea()