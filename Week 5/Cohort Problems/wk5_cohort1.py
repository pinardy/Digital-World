import random
import time
random.seed(round(time.time()/3,-1))   #do not seed elsewhere in your code

#################################
#       SMALLER FUNCTIONS       #
#################################

craps=set([2,3,12])
naturals=set([7,11])

def rollTwoDices():
    n1=random.randint(1,6)
    n2=random.randint(1,6)
    return n1,n2
def isCraps(n):    
    return n in craps  # returns a BOOLEAN 
def isNaturals(n):
    return n in naturals  # returns a BOOLEAN
def printWin():
    return 'You win'
def printLose():
    return 'You lose'
def printPoint(point):
    print 'point is ',point

        
#################################
# ------- MAIN FUNCTION ------- #

def playCraps():
    #finish=False
    point=-1
    #while not finish:
    while True:
        n1,n2=rollTwoDices()
        sumn=n1+n2
        print 'You rolled %d + %d = %d'%(n1,n2,sumn)
        if point ==- 1:
            if isCraps(sumn):
                return printLose()
            elif isNaturals(sumn):
                return printWin()
            point=sumn
            printPoint(point)
        else:
            if sumn==7:
                return printLose()
            elif sumn == point:
                return printWin()
                
print playCraps()
            
