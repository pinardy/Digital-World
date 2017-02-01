""" Write a function that reads in a file object and replaces text inside the
opened file. The header of the function should takes in the file object, an old string, and
a new string. The function should return the new text as a string where the new string
input argument replaces the old string in the text. Use file 'replace.txt' to test. """

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
#    for line in f1:
#        f2.write(line.replace(oldS, newS))
#    file1 = f1
#    f1.close()
#    f2.close()
#    return f2
f = open('replace.txt',"r")
##-------------------------------------##
def replace(f, oldS, newS):

    x = f.read()
    x = x.replace(oldS,newS)
    return x

print replace(f,'Title: The Sign of the Four','Title: The Sign of the One')