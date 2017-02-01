#import urllib2
#
#data = urllib2.urlopen("http://www.google.com").read(20000) # read only 20 000 chars

#for line in data:
#    print line.split()

f=open("level1_1.inp.txt","r")
lines = f.readlines()
#print lines

shippingDict={}
for line in lines:
    print line.split()
    x=line.split()
    shippingDict[x[0]]=int(x[1])
print shippingDict
    