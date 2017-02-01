def findAnagram(f):
    d={}
    dAnagram={}
    seen=[]
    for line in f:
        word=line.strip()
        lenWord=len(word)
        if lenWord not in d:    #check key only
            d[lenWord]=[word]
        else:
            d[lenWord]+=[word]  #add a new string to dictionary

    for l in d:                 # l is key
        if l > 1 and len(d[l]) > 1:
            dEachLen={}
            for word in d[l]:
                x=tuple(sorted(list(word)))
                if x not in dEachLen:
                    dEachLen[x]=[word]
                else:
                    dEachLen[x]+=[word]
            for eachSet in dEachLen:
                l=len(dEachLen[eachSet])
                if l not in dAnagram:
                    dAnagram[l]=[dEachLen[eachSet]]
                else:
                    dAnagram[l]+=[dEachLen[eachSet]]
            
    maxFreq=max(dAnagram.keys())
    return dAnagram[maxFreq]