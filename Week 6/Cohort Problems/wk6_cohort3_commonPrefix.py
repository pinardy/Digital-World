def prefix(s1,s2):
    output = ''
    length = min(len(s1),len(s2))
    for i in range(length):
        if s1[i] == s2[i]:
            output += s1[i]
        else:
            break
    return output
  
print prefix('drinking','drinker')
#prefix('drinking','drinker')