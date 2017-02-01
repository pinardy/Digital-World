##Qn2
#def isValidPassword(password):
#    if (len(password) >= 8):
#        if password.isalnum():
#            num = 0
#            
#            for i in password:
#                if i.isdigit():
#                    num += 1
#            if num > 1:
#                return True
#            else:
#                return False
#        else:
#            return False
#    else:
#        return False
#

##Qn 3 
#def prefix(s1,s2):
#    output = ''
#    length = min(len(s1),len(s2))
#    for i in range(length):
#        if s1[i] == s2[i]:
#            output += s1[i]
#        else:
#            break
#    
#    
#    return output
#    
#    
#print prefix('drinking','drinker')

##Qn 4
#class Coordinate:
#    x=0
#    y=0
#f = open('xy.dat','r')
#def read2columns(f):    
#    max1 = 0
#    min1 = 0
#    pmax = Coordinate()
#    pmax.x = 0
#    pmax.y = 0
#    pmin = Coordinate()
#    pmin.x = 0
#    pmin.y = 0
#    for n in f:
#        coord = n.split()
#        x = float(coord[0])
#        y = float(coord[1])
#        #print x 
#        #print coord
#        p = ( x**2 + y**2 )**0.5
#        #print p
#        if p > max1:
#            max1 = p
#            pmax.x = x
#            pmax.y = y
#        elif p<= min1:
#            min1 = p 
#            pmin.x = x
#            pmin.y = y
#    return pmax,pmin
#        
#    
#
##print read2columns(f)
#
#pmax , pmin = read2columns (f)
#print 'max : (% f , % f )' %( pmax .x , pmax . y )
#print 'min : (% f , % f )' %( pmin .x , pmin . y )
#
#         

#Qn 5
#def replace(f, oldS, newS):
#    #f = open(f,"w")
#    #f = f.replace(oldS,newS)
#    #return f
#
##    f = open(f,'r')
##    filedata = f.read()
##    f.close()
##
##    newdata = filedata.replace(oldS,newS)
##
##    s = open(f,'w')
##    s.write(newdata)
##    return newdata
#    f1 = open(f, 'r+')
#    f2 = open(f, 'w')
#    print f2
#    for line in f2:
#        print line
#    #for line in f1:
#    #    f2.write(line.replace(oldS, newS))
#    #file1 = f1
#    #f1.close()
#    #f2.close()
#    return f2
#    
#    
#def replace(f, oldS, newS):
#
#    f = f.read()
#    f = str(f).replace(oldS,newS)
#    return f
#
#print replace('replace.txt','Title: The Sign of the Four','Title: The Sign of the One')

#Hw Qn 1
#def binaryToDecimal(binaryString):
#    
#    decimal = 0
#    for i in binaryString:
#        decimal = decimal*2 +int(i)
#    return decimal
#
#print binaryToDecimal('100')

#HW Qn 2
#def uncompressed(s):
#    
#    a = 0
#    uncompressed = ""
#    for i in s:
#        if i.isdigit():
#            a = int(i)
#        else:
#            uncompressed += i*a
#            
#    return uncompressed
#    
#    
#print uncompressed('2d3c')
#        
#    
#HW Qn 3    
#import string
#UpperCase = string.ascii_uppercase
#
#def getBaseCounts2(dna):
#    validDNA = ['A','T','C','G']
#    d = {'A':0,'T':0,'C':0,'G':0}
#    for i in dna:
#        if i.islower():
#            return "The input DNA string is invalid"
#           
#        elif i in validDNA:
#                d[i] += 1
#          
#            
#    return d
#        
#print getBaseCounts2('AATLLQC')
#    
    
#HW Qn 4
#def constants():
#    f = open('constants.txt','r')
#    d = dict()
#    lines = f.readlines()[2:]
#    for x in lines:
#        constant,value,unit = x.split()
#        value = float(value)
#        d[constant] = value
#
#
#    return d
#    
#    
#print constants()
    
    
##HW Qn 5
#def processScores():
#    f = open('scores.txt','r')
#    scores = f.read().splitlines()
#    counter = 0
#    sum1 = 0
#    #scores = scores.split('\r')
#    for x in scores:
#        x = float(x)
#
#        sum1 += x
#        counter +=1
#    average = sum1/counter
#    return average
#    return scores
#
#print processScores()
#    
#HW Qn 5 Alternative ans    
#def scores(f):
#    scores = f.read().splitlines()
#    counter = 0
#    sum1 = 0
#    for x in scores:
#        x = float(x)
#
#        sum1 += x
#        counter +=1
#    average = sum1/counter
#    return sum1,average

    
    