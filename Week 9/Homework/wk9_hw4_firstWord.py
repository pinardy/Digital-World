import libdw.sm as sm
myList=[]
class FirstWordSM(sm.SM):
    startState = 'first'
    
    def getNextValues(self, state, inp):
    	#myList=[]
        if state == 'first':
        	#can use list to keep track of last char
        	if inp != ' ' and inp != '\n':
        		nextState=state
        		out=inp
        		myList.append(inp)
        	elif inp == ' ':
        		if myList[-1] not in [' ','\n']:
        			nextState='notFirst'
        			out=None
        			myList.append(inp)
        		else:
        			nextState=state
        			out=None
        			myList.append(inp)
       		elif inp == '\n': 
       			nextState=state
       			out=None
       			myList.append(inp) 

       		return nextState, out

       	if state == 'notFirst':
       		if inp != '\n':
       			nextState ='first'
       			out=None
       			myList.append(inp)
       		else:
       			nextState=state
       			out=None
       			myList.append(inp)

       		return nextState, out

x = '''This is the
time for

 all good 
men to come to the
  aid of their country'''
meow = FirstWordSM()
print FirstWordSM().transduce(x)