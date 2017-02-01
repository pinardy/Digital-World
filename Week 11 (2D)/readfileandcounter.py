#==================#
f=open("level1_1.inp.txt","r")
lines = f.readlines()
shippingDict={}
for line in lines:
    # print line.split()
    x=line.split()
    shippingDict[x[0]]=int(x[1])
print shippingDict

# shippingDict: {'A': '6', 'C': '4', 'B': '2'}

#================================#
#======== COUNTER CODE ==========#
counterA=0
counterB=0
counterC=0

exactDivA= float(shippingDict['A'])/6
counterA=shippingDict['A']/6
if exactDivA > shippingDict['A']/6:
    counterA+=1

exactDivB= float(shippingDict['B'])/6
counterB=shippingDict['B']/6
if exactDivB > shippingDict['B']/6:
    counterB+=1

exactDivC= float(shippingDict['C'])/6
counterC=shippingDict['C']/6
if exactDivC > shippingDict['C']/6:
    counterC+=1

print counterA, counterB, counterC