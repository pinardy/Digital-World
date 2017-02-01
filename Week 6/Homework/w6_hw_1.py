def binaryToDecimal(binaryStr):
    output=0
    counter=-1
    for i in binaryStr[::-1]:
        counter+=1
        if i == '1':
            output+=2**counter
    return output
        
    
print binaryToDecimal('10101')