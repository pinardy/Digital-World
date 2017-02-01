def isValid(num):
    x = str(num)   
    sumSingleDigits=0
    sumOddDigits=0
    
    for i in x[-2::-2]:
        #print i
        if len(i) >2:
            
        else:
            sumSingleDigits += int(i) *2
        
    #print sumSingleDigits
    for i in x[-1::-2]:
        sumOddDigits += int(i)
    #print sumOddDigits
    neededSum = sumSingleDigits + sumOddDigits
    #print neededSum
    if neededSum%10 == 0:
        return True
    else:
        return False

#isValid(5411045872559122)
#print isValid(5411045872559122)
isValid(4388576018402626)
#isValid(6011432717792989)
        