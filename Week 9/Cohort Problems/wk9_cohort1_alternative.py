from libdw import sm

class CokeMachine(sm.SM):
	startState=0 # no coin

	def getNextValues(self,state, inp): 
		if state==0: 
			if inp==100:
				output=(0,"coke",0)
				nextState=0
			elif inp==50:
				output=(50,'--',0)
				nextState=1
			if inp!= 50 and inp!= 100:
				output=(0,'--',inp)
				nextState=state

		if state==1:
			if inp==100:
				output=(0,'coke',50)
				nextState=0
			if inp==50:
				output=(0,'coke',0)
				nextState=0
			# else: # CANNOT USE ELSE
			if inp!= 50 and inp!= 100:
				output=(50,'--',inp)
				nextState=state

		return nextState, output


c=CokeMachine()
c.start()
# print c.step(50)
# print c.step(10)
# print c.step(10)

print c.transduce([50,100,50,10,20])