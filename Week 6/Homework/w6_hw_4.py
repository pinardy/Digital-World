f = open('constants.txt','r')
def fundamentalConstants(f):
    d = {}
    lines = f.readlines()[2:]
    for x in lines:
        constant,value,unit = x.split()
        value = float(value)
        d[constant] = value

    return d
    
print fundamentalConstants(f)
