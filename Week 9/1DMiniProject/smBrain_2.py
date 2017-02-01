import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    startState=0
    def getNextValues(self, state, inp):
        print inp.sonars# list
        print inp.odometry.theta
        #state=0 --> eBot has not reach near wall.
        #state=1 --> eBot has reached near wall
        if state==0 and inp.sonars[2]<0.4:
            state=1
            return (state, io.Action(fvel = -0.05, rvel = 0.00))
        elif state==0 and inp.sonars[2]>0.45 and inp.sonars[2]<0.55:
            state=1
            return (state, io.Action(fvel = 0.00, rvel = 0.00))
        elif state==0 and inp.sonars[2]>0.6:
            state=1
            return (state, io.Action(fvel = 0.05, rvel = 0.00))
        elif state==1 and inp.sonars[2]<0.4:
            state=1
            return (state, io.Action(fvel = -0.05, rvel = 0.00))
        elif state==1 and inp.sonars[2]>0.45 and inp.sonars[2]<0.55:
            state=0
            return (state, io.Action(fvel = 0.00, rvel = 0.00))
        elif state==1 and inp.sonars[2]>0.55:
            state=0
            return (state, io.Action(fvel = 0.05, rvel = 0.00))
        
        return (state, io.Action(fvel = 0.05, rvel = 0.0))

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
