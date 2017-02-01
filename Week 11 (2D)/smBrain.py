import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io
import time
import urllib2


class MySMClass(sm.SM):
 
    # data = urllib2.urlopen("http://www.google.com")
    # for line in data:
    #   print line.split()

    #========#
    f=open("level1_1.inp.txt","r")
    lines = f.readlines()
    shippingDict={}
    for line in lines:
        print line.split()
        x=line.split()
        shippingDict[x[0]]=int(x[1])

    # shippingDict: {'A': '6', 'C': '4', 'B': '2'}

    #========#

    startState='start'

    def getNextValues(self, state, inp):
        #---Printing data---#
        data = inp.sonars
        an = inp.analogInputs
        od = inp.odometry
        temp = inp.temperature
        ldr = inp.light
        print '-----'
        print data
        print an
        print od
        print 'Temp: ', temp
        print ldr
        #--------------------#
        # ----- STATES ----- #
        # States: start, forward, rotate, stop
        

        if state=='start' and inp.sonars[2]>0.45:
            nextState='forward'
            fwd = 0.1
            rev = 0.00

        elif state=='forward' and inp.sonars[2]<0.75:
            nextState='stop'
            dDesired = 0.55
            dSensed=inp
            e=dDesired-dSensed
            v=k*e
            k= -0.7 # -0.7, -20, -40
            fwd = v
            rev = 0.00

        # elif state=='stop':
        #     #>>> CODE FOR WAITING 8s <<<
        #     nextState='rotate'

        # elif state=='rotate':


        #--------------------#
        return nextState, io.Action(fvel = fwd, rvel = rev)

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
    # print inp.sonars[3]
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())

# called when the stop button is pushed
def brainStop():
    pass

# called when brain or world is reloaded (before setup)
def shutdown():
    pass
