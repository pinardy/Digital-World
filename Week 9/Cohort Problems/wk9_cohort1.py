from libdw import sm

class CM(sm.SM):
    startState=0
    def getNextValues(self,state, inp):   
        if state==0 and inp==100:
            nextState=0
            output=(0,'coke',0)
        elif state==0 and inp==50:
            nextState=1
            output=(50,'--',0)
        elif state==1 and inp==100:
            nextState=0
            output=(0,'coke',50)
        elif state==1 and inp==50:
            nextState=0
            output=(0,'coke',0) 
        elif inp!=100 and inp!=50:
            if state==1:
                nextState=state
                output=(50,'--',inp)
            elif state==0:
                nextState=state
                output=(0,'--',inp)
            
        
        return nextState, output
c=CM()
c.start()
#print c.step(50)
#print c.step(10)
#print c.step(100)

print c.transduce([50,100,50,10,20])