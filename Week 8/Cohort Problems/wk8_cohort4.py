########## Define your class Line below this line ###########
class Line:
	def __init__(self,c0,c1):
		self.c0=float(c0)
		self.c1=float(c1)

	def __call__(self,x):
		return round(self.c0+self.c1*x,1)

	def table(self,a,b,n):
		step = (b-a)/(n-1)
		output=''
		x=a
		if n==0 and a!=b:
			for i in range(n):
				y=self.__call__(x)
				output+='%10.2f%10.2f\n'%(x,y)
				x+=step
		elif a==b:
			x=a
			y=self.__call__(x)
			output+='%10.2f%10.2f\n'%(x,y)
		else:
			output+='Error in printing table'
		return output

# l1=Line(1,2)
# print l1(1)
#

########## Ignore the code below this line ##################

def testLine(c0,c1,x,L,R,N):
    line=Line(c0,c1)
    return line(x),line.table(L,R,N)

print testLine(1,2,2,1,5,4)