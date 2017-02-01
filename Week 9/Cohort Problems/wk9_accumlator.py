from libdw import sm

class Accumulator(sm.SM):
	startState=0

	def getNextValues(self, state, inp):
		nextState=state+inp
		output=state+inp
		return nextState, output

a=Accumulator()
inp=[10,20,5,-2,11,-3]
print a.transduce(inp)
