""" DNA:Write a function named getBaseCounts2() by modifying getBaseCounts()
that you wrote in homework problem set 4. getBaseCounts2() takes a string as input.
The input string may contain letters other than A, C, G, and T. The function should
return the counts of only A, C, G, and T in the form of a dictionary; it must ignore all
letters other than A, C, G, and T. For any input string with lower case alphabets, the
function will still return `The input DNA string is invalid'. """

def getBaseCounts2(dna):
    countA=0
    countT=0
    countC=0
    countG=0
    resultdict={}
    for i in dna:
        if i=='A':
            countA+=1
        elif i=='T':
            countT+=1
        elif i=='C':
            countC+=1
        elif i=='G':
            countG+=1
        elif i=='a' or i=='t' or i=='c' or i=='g':
            return 'The input DNA string is invalid'
        else:
            pass
    if countA > 0:
        resultdict['A']=countA
    if countT > 0:
        resultdict['T']=countT
    if countC > 0:
        resultdict['C']=countC
    if countG > 0:
        resultdict['G']=countG

    if countA == 0:
        resultdict['A']=0
    if countT == 0:
        resultdict['T']=0
    if countC == 0:
        resultdict['C']=0
    if countG == 0:
        resultdict['G']=0
    
    return resultdict
    
# print getBaseCounts2('AACCGT')
# print getBaseCounts2('AAB')
# print getBaseCounts2('AaCaGT')
# print getBaseCounts2('A')
print getBaseCounts2('AAAGGIII')
print getBaseCounts2('ADLSTTLLD')
