import math
import sys

class Coordinate:  # a class is to create a custom data type
    x=0
    y=0

def read2columns(f):
    #for line in f:
        #print line
    #return None, None
    
    pmax=-sys.maxint
    pmin=sys.maxint
    pm1=Coordinate()
    pm2=Coordinate()
    
    lines = f.readlines()
    for line in lines:
        #print line
        data = line.split()
        #print data
        p=Coordinate()
        p.x=float(data[0])
        p.y=float(data[1])
        #print p.x, p.y
        
        mag = math.sqrt((p.x)**2.0 + (p.y)**2.0)
        #print mag
        if mag > pmax:
            pmax = mag
            pm1=p
        if mag < pmin:
            pmin = mag
            pm2=p
            
    return pm1, pm2
    
    
f=open('xy.dat','r')  # 'r' is the mode (Read) 
pmax,pmin=read2columns(f)
#print pmax.x,pmax.y
#print pmax.x,pmin.y
print 'max: (%f, %f)'%(pmax.x,pmax.y)
print 'min: (%f, %f)'%(pmin.x,pmin.y)


