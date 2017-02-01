from libdw import sm

class BitCounter(sm.SM):
	startState=(0,0)

	def getNextValues(self, state, inp):
		if inp==1:
			output=(state[0], state[1]+1)
		else:
			output=(state[0]+1, state[1])
		nextState = output  # this statement is standard

		return nextState, output
		# return nextState   <--- cannot just return nextState.
		#					 Need to return both nextState and output

a=BitCounter()
inp=[1,1,0,0,0,0]
print a.transduce(inp)