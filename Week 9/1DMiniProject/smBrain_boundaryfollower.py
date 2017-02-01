import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    # states:  nearWall, notNearWall
    startState='notNearWall'
     
    def getNextValues(self, state, inp):
        print inp.sonars # list
        print inp.odometry.theta

        if state=='notNearWall' and inp.sonars[2]>0.6:
            nextState=state
            fwd=0.05
            rev=0.00
        elif state=='notNearWall' and 0.45<inp.sonars[2]<0.55: # moving in empty space
            nextState=nearWall
            fwd=0.00
            rev=0.05 # <--- must be ACW
        elif state=='nearWall' and inp[2]>0.55 and inp[4]<0.45: # moving along wall
            nextState=state
            fwd=0.05
            rev=0.05
        elif state=='nearWall' and inp[2]>0.55 and inp[4]>0.55: # moving along wall
            nextState=state
            fwd=0.05
            rev= -0.05 # <--- CW
        elif state=='nearWall' and inp[2]>0.6 and inp[4]>0.6: # outer corner
            nextState=state
            fwd=0.00
            rev=-0.05
        elif state=='nearWall' and inp[2]<0.45 and inp[4]<0.45: # inner corner
            nextState=state
            fwd=0.00
            rev=0.05 # <--- must be ACW
        else:
            fwd=0.00
            rev=0.00
            nextState=state

            
        return nextState, io.Action(fvel=fwd,rvel=rev)

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
    print inp.sonars[3]
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())

# called when the stop button is pushed
def brainStop():
    pass

# called when brain or world is reloaded (before setup)
def shutdown():
    pass
