''' takes a compressed string as input and outputs an uncompressed string, 
where each alphabetic character is preceded by a single digit indicating 
the number of times that the character should be entered in the
uncompressed version of the string '''

def uncompressed(s):
    listNum=[]
    listLetter=[]
    for i in s:
        #print i.isdigit()
        if i.isdigit():
            listNum.append(i)
        else:
            listLetter.append(i)
    #print listNum
    #print listLetter
    #x = dict(zip(listLetter,listNum))  #uses zip method instead
    #print range(len(listLetter))
    x = {listLetter[n]: listNum[n] for n in range(len(listLetter))}
    #print x
    output_unsorted=''
    for i in x:
        output_unsorted+=i*int(x[i])
    #print output_unsorted
    output=''
    for j in sorted(output_unsorted):
        output+=j
    return output
        
            
#uncompressed('2a5b1c')    # ANS: aabbbbbc 
print uncompressed('2a5b1c')

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