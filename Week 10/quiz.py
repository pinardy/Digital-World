from libdw import sm

class RunOfFive(sm.SM):
    startState = 0 #notfive  
    
    def getNextValues(self, state, inp):
        if inp!=5:
            nextState=0
            output=0
        else:
            nextState=state+1
            output=nextState              
        
        return nextState, output

m=RunOfFive()
m.transduce([2,5,0,2,5,5,0,5,7])
print m.transduce([2,5,0,2,5,5,0,5,7])