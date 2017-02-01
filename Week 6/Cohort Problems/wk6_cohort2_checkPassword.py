def isValidPassword(password):
    if len(password)<8:
        return False
    if password.isalnum() == False:
        return False
    digitcounter=0
    for i in password:
        if i.isdigit()==True:
            digitcounter+=1
    #print digitcounter
    if digitcounter<2:
        return False
    else: 
        return True
    



print isValidPassword('test')
print isValidPassword('testtest')
print isValidPassword('testt22')
print isValidPassword('testte22')