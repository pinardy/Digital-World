#def maxList(a):
#    if a == []:
#        return (None, None)
#    else:
#        x = a[0]
#        y = a[0]
#        for i in a:
#            print i
#    return (x, y)
#print maxList([5,12,33,15,21]) 

l=[1,2,3] 
#l[2:3]=4 # (a)


l[1:3]=[0] # (b) 
#l[1:1]=1 #(c) 
l[2:]=[] # (d)
print l