def isValidPassword(password):
    if len(password)>=8:
        if password.isalnum():
            num=0
            for i in password:
                if i.isdigit():
                    num+=1
                if num>1:
                    return True
                else:
                    return False
            else:
                return Falsee
        else:
            return False
            
print isValidPassword('test')
print isValidPassword('testtest')
print isValidPassword('testt22')
print isValidPassword('testte22')