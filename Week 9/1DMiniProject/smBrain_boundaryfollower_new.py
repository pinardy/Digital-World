import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    # states:  start, line, turn, adjust
    startState='start'
     
    def getNextValues(self, state, inp):
        print inp.sonars # list
        print inp.odometry.theta
    #----------------------------------------# 
    #--- start to turn transitions --- #    
        if state=='start' and inp.sonars[2]>0.6:
            nextState='start'
            fwd=0.2
            rev=0.00
        elif state=='start' and inp.sonars[2]<0.4:
            nextState='turn'
            fwd=0.00
            rev=-0.5 #acw
    #----------------------------------------# 
    #--- turn to line transitions (vice versa)--- #
        elif state=='turn' and inp.sonars[2]>0.4 and inp.sonars[4]<0.4:
            nextState='line' # along the wall
            fwd=0.2
            rev=0.00
        elif state=='line' and inp.sonars[2]>0.4 and inp.sonars[4]>0.4:
            nextState='turn'  # outer corner, turn right
            fwd= 0.00
            rev= -2  
        elif state=='line' and inp.sonars[2]<0.4 and inp.sonars[4]>0.4:
            nextState='turn'  # going straight, hit wall, turn left 
            fwd= 0.00
            rev=2
        elif state=='line' and inp.sonars[2]<0.4 and inp.sonars[4]<0.4:
            nextState='turn'  # inner corner, turn left 
            fwd= 0.00
            rev=1
    #----------------------------------------#
    #----- ADJUSTING ------------------------#
        elif state=='line' and inp.sonars[3]<0.4 and inp.sonars[2]<0.6:
            nextState='adjust'  # skew right from wall
            fwd= 0.03
            rev= 1  
        elif state=='line' and inp.sonars[2]>0.4 and inp.sonars[4]<0.3:
            nextState='adjust'  # skew left from wall
            fwd= 0.03
            rev= -1   
        elif state=='adjust' and inp.sonars[2]>0.4 and inp.sonars[4]<0.3:
            nextState='adjust'  
            fwd= 0.1
            rev= 0.00
        else:
            nextState='line'
            fwd=0.2
            rev=0.00  

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
