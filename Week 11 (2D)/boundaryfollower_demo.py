import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    # states:  start, leftTurn, rightTurn
    startState='start'
     
    def getNextValues(self, state, inp):
        print inp.sonars # list
        print inp.odometry.theta

        if state=='start':
            fwd=0.1
            rev=0.05
            if inp.sonars[1]<0.4:
                nextState='leftTurn'
            elif inp.sonars[2]<0.4:
                nextState='leftTurn'
            else:
                nextState='start'

        elif state=='leftTurn':
            fwd=0.08
            rev=0.35
            if inp.sonars[3]<0.4:
                nextState='leftTurn'
            elif inp.sonars[2]>0.45 and inp.sonars[4]>0.3:
                nextState='rightTurn'
            else:
                nextState='leftTurn'
            
        elif state=='rightTurn':
            fwd=0.08
            rev=-0.3
            if inp.sonars[3]<0.4:
                nextState='leftTurn'
            elif inp.sonars[4]<0.35:
                nextState='leftTurn'
            elif inp.sonars[2]<0.5:
                nextState='leftTurn'    
            else:
                nextState='rightTurn'
            
                
            
    #----------------------------------------#      
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
