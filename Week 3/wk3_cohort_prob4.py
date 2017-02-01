def listSum():
    list = raw_input('What is your list of numbers? Separate them with spaces)')
    ans=listSum(list)
    sum = 0.0
    for x in ans:
        sum += x
    return sum
    
listSum()