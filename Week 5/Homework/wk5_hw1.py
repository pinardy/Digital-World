#def getData():
#    inp=raw_input('Enter integer pair (hit Enter to quit): ')
#    
    

#def extractValues(values):
#    values = values.split()
#    values = [int(i) for i in values]
#    return tuple(values)
   
def extractValues(values):
    values = values.split()
    #print values
    output=()
    for num in values:
        output+=(int(num),)
    return output
    
    #values = [int(i) for i in values]
    #return tuple(values)

#print extractValues('123 456')

def calcRatios(values):
    if values[1]==0:
        return None
    else:
        a=float(values[0])
        b=float(values[1])
        ratio = a/b
        return ratio
        
print calcRatios((134, 289))
