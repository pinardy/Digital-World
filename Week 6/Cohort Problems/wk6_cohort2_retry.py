def isValidPassword(password):
    if len(password) < 8:
        return False
    if not password.isalnum():
        return False
    count=0
    for i in password:
        if i.isdigit():
            count+=1
    if count < 2:
        return False
    else:
        return True
        
print isValidPassword('test')
print isValidPassword('testtest')
print isValidPassword('testt22')
print isValidPassword('testte22')