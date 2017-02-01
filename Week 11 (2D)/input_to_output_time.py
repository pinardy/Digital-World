import time

#f = open("output.txt","a") #opens file with name of "test.txt"
#f.write("and can I get some pickles on that")
#f.close()

localtime = time.localtime(time.time())
#print "Local current time :", localtime
print localtime[1]