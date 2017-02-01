import libdw.sm as sm
class CommentsSM(sm.SM):
	# 0: not a comment
	# 1: a comment
    startState = 0 

    def getNextValues(self, state, inp):
        if state == 0:
        	if inp == '#':
        		nextState=1
        		return nextState,'#'
        	else:
        		return state, None

        elif state == 1:
        	if inp == '\n': 
        		state=0
        		return state, None
        	else:
        		return state, inp
