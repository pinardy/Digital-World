def getDigit(number):
    x=str(number)
    if len(x) == 1:
        return x
        #print x
    else:
        ans=0
        for i in x:
            ans+= int(i)
        return ans
        
        
print getDigit(2) #ans is 2
print getDigit(12) #ans is 3