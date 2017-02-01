import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    startState='line'
    
    def getNextValues(self, state, inp):     
        #print inp.sonars# list
        fwd = 0 # fvel
        rev = 0 # rvel
        if state == 'turnleft':
            rev = -0.5 # CW
            fwd = 0.2
            if inp.sonars[3] < 0.2 and inp.sonars[4] < 0.3:  #CHANGED AND TO OR
                state = 'line'
        if state == 'adjusting':
            rev = 0.3 # ACW
            if inp.sonars[2] > 0.3 or inp.sonars[2] < 0.2:
                state = 'line'
                rev = 0.1 # ACW
        if state == 'line':
            if inp.sonars[2] < 0.4 and inp.sonars[2] > 0.2:
                print "STOP"
                fwd = 0
                rev = 0.75 # ACW
                state ='wallturn'
            elif inp.sonars[2] < 0.4:
                print "BACK"
                fwd = -(inp.sonars[2]**2+0.5)/10
                if fwd < -0.3:
                    fwd = -0.3
                rev = 0
                state = 'line'
            elif inp.sonars[2] > 0.2:
                print "FORWARD"
                fwd = (inp.sonars[2]**2+0.5)/10
                if fwd > 0.3:
                    fwd = 0.3
                rev = 0
                state = 'line'
                if state == 'line' and inp.sonars[3] > 3 and inp.sonars[4] < 0.3:
                    state = 'turnleft'
                    fwd = 0.4
                    rev = -1 # CW
                if inp.sonars[3] < 0.5 and inp.sonars[4] < 0.3:
                    state = 'adjusting'
                    fwd = 0
                    rev = 1 # ACW
        if state == 'wallturn':
            if inp.sonars[4] > 0.4:
                rev = 0.75 # ACW
                state = 'wallturn'
            if inp.sonars[4] < 0.4 or inp.sonars[3] < 0.4:
                state = 'line'
                
        print 'Front',inp.sonars[2]
        print 'LDiag', inp.sonars[1]
        print 'LSide', inp.sonars[0]
        print 'RDiag', inp.sonars[3]
        print 'RSide', inp.sonars[4]
        print 'fvel', fwd
        print 'rvel', rev
        print state
        return (state, io.Action(fvel = fwd, rvel = rev))
        #print inp.odometry.theta

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
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False, # slime trails
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
