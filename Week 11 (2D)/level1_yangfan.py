import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io
import time
import firebase

def getRoute(f):
    lines=f.readlines()
    goal={}
    route=['H','X']
    for i in lines:
        x=[]
        x+=i.split()
        goal[x[0]]=x[1]
    for n in sorted(goal.keys()):
        route+=([n]+['X'])*((int(goal[n])-1)/6+1)
    return route


url = "https://gintaka.firebaseio.com/" # URL to Firebase database
token = "74Dm9anUkDBN91Wb2O39FWdch5d2JcH9yBMLSpqB" # unique token used for authentication
firebase = firebase.FirebaseApplication(url, token)
f=open('level1_2.inp','r')
route=getRoute(f)

class MySMClass(sm.SM):
    startState=['forward']+[[route]]+[time.time()]
    def getNextValues(self, state, inp):
       
        data = inp.sonars
        an = inp.analogInputs
        od = inp.odometry
        temp = inp.temperature
        ldr = inp.light
        leftAngle=float(data[1])/float(data[0])
        rightAngle=float(data[3])/float(data[4])
        

        if state[0]=='forward':
            if data[2]<=0.7:
                if len(state[1][0])==1:
                    output=io.Action(0.0,0.0)
                    state=['stop']+[state[1]]+[time.time()]
                else:
                    output=io.Action(0.0, 0.0)
                    outputTime=time.strftime("%H:%M:%S|%d/%b/%Y", time.gmtime())
                # firebase.put('/','Station/ldr',ldr[0])
                #firebase.put('/','Station/temp',temp)
               # firebase.put('/','Station/time',outputTime)
                    route=state[1][0][1:]
                    state=['wait']+[[route]]+[time.time()]
            elif data[0]>=5 and data[4]>=5 and data[2]>=5 and state[1][0][0]!='H':
                output=io.Action(0.2, 0.0)
                state=['turn']+[state[1]]+[time.time()]
            else:
                output=io.Action(0.2, 0.0)
                state=['forward']+[state[1]]+[time.time()]
        if state[0]=='turn':
            output=io.Action(0.2, 0.0)
            if state[1][0][0]=='A':
                if state[1][0][1]=='C':
                    state=['forward']+[state[1]]+[time.time()]
                elif state[1][0][1]=='B':
                    state=['turnRight']+[state[1]]+[time.time()]
                elif state[1][0][1]=='X':
                    state=['turnLeft']+[state[1]]+[time.time()] 
            if state[1][0][0]=='B':
                if state[1][0][1]=='X':
                    state=['forward']+[state[1]]+[time.time()]
                elif state[1][0][1]=='C':
                    state=['turnRight']+[state[1]]+[time.time()]
                elif state[1][0][1]=='A':
                    state=['turnLeft']+[state[1]]+[time.time()] 
            if state[1][0][0]=='C':
                if state[1][0][1]=='A':
                    state=['forward']+[state[1]]+[time.time()]
                elif state[1][0][1]=='X':
                    state=['turnRight']+[state[1]]+[time.time()]
                elif state[1][0][1]=='B':
                    state=['turnLeft']+[state[1]]+[time.time()] 
            if state[1][0][0]=='X':
                if state[1][0][1]=='B':
                    state=['forward']+[state[1]]+[time.time()]
                elif state[1][0][1]=='A':
                    state=['turnRight']+[state[1]]+[time.time()]
                elif state[1][0][1]=='C':
                    state=['turnLeft']+[state[1]]+[time.time()] 
        if state[0]=='wait':
            output=io.Action(0.0,0.0)
            if time.time()<state[-1]+8:
                state=['wait']+[state[1]]+[state[-1]]
            else:
                state=['turnRound']+[state[1]]+[time.time()]
        if state[0]=='turnRound':
            if data[2]>=5 and rightAngle>=leftAngle:
                output=io.Action(0.2, 0.0)
                state=['forward']+[state[1]]+[time.time()]
            else:
                output=io.Action(0.0, 0.1)
                state=['turnRound']+[state[1]]+[time.time()]
        if state[0]=='turnLeft':
            if data[2]>=5 and data[4]<5 and data[1]>=data[3]:
                output=io.Action(0.2,0.0)
                state=['forward']+[state[1]]+[time.time()]
            else:
                output=io.Action(0.1, 0.135)
                state=['turnLeft']+[state[1]]+[time.time()]
        if state[0]=='turnRight':
            if data[2]>=5 and data[0]<5 and data[3]>=data[1]:
                output=io.Action(0.2,0.0)
                state=['forward']+[state[1]]+[time.time()]
            else:
                output=io.Action(0.1, -0.135)
                state=['turnRight']+[state[1]]+[time.time()]
        if state[0]=='stop':
            output=io.Action(0.0,0.0)
        print data,state
        #print an
        #print od
        #print temp
        #print ldr

        return (state, output)
        #return (state, io.Action(fvel = 0.05, rvel = 0.05))

mySM = MySMClass()
mySM.name = 'brainSM'



######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar'+str(sonarNum),
                                        lambda: 
                                        io.SensorInput().sonars[sonarNum]))

# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=True, # slime trails
                                  sonarMonitor=False) # sonar monitor widget
    
    # set robot's behavior
    robot.behavior = mySM

# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks = robot.gfx.tasks())

# this function is called 10 times per second
def step():
    inp = io.SensorInput()
    # print inp.sonars[3]
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())

# called when the stop button is pushed
def brainStop():
    pass

# called when brain or world is reloaded (before setup)
def shutdown():
    pass
