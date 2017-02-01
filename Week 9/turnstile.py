import libdw.sm as SM
class Turnstile1(SM):
    startState = 'locked'
    def getNextValues(self, state, inp):
        if state == 'locked':
            if inp == 'coin':
                return ('unlocked', 'enter')
            else:
                return (Q3, Q4)
        else:                           # state == 'unlocked'
            if inp == 'turn':
                return (Q5, Q6)
            else:
                return (Q7, Q8)