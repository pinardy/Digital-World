counterA=0
counterB=0
counterC=0
shippingDict={'A':13, 'B':7, 'C':6}


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

counterList=[counterA,counterB,counterC]   

print counterList

