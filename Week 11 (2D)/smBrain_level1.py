import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io
import time
import urllib2
import firebase
from eBot import eBot
from time import sleep

url = "https://pinardy.firebaseio.com/" # URL to Firebase database
token = "4vlssuGd2ljBfQSy07CKFIqhEIpd7LcFMunm6Jmj" # unique token used for authentication
firebase = firebase.FirebaseApplication(url, token)

class MySMClass(sm.SM):
 
    # data = urllib2.urlopen("http://www.google.com")
    # for line in data:
    #   print line.split()

    #==================#
    f=open("level1_1.inp.txt","r")
    lines = f.readlines()
    shippingDict={}
    for line in lines:
        # print line.split()
        x=line.split()
        shippingDict[x[0]]=int(x[1])

    # shippingDict: {'A': '6', 'C': '4', 'B': '2'}

    #================================#
    #======== COUNTER CODE ==========#
    counterA=0
    counterB=0
    counterC=0
    shippingDict={'A':13, 'B':7, 'C':6}


    exactDivA= float(shippingDict['A'])/6
    counterA=shippingDict['A']/6
    if exactDivA > shippingDict['A']/6:
        counterA+=1

    exactDivB= float(shippingDict['B'])/6
    counterB=shippingDict['B']/6
    if exactDivB > shippingDict['B']/6:
        counterB+=1

    exactDivC= float(shippingDict['C'])/6
    counterC=shippingDict['C']/6
    if exactDivC > shippingDict['C']/6:
        counterC+=1


    #================================#

    startState='reload'

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
        print "--Trips left--"
        # print 'A: ',counterA, 'B: ',counterB, 'C: ',counterC
        #--------------------#
        # ----- STATES ----- #
        # States: reload, reloading, search, rotate
        
        if state=='reload':
            if inp.sonars[2]>0.75:
                fwd = 1.5
                rev = 0.0
                nextState=state
            elif inp.sonars[2]<0.75:
                #SLOWDOWN CODE HERE
                dDesired = 0.45
                dSensed=inp
                e=dDesired-dSensed
                v= -20*e
                fwd = v
                rev = 0.0
                nextState='reloading'

        elif state=='reloading':
            sleep(8)
            nextState='rotate'

        elif state=='rotate':
            if inp.sonars[2]<0.8:
                fwd=0
                rev=1
                nextState=state
            elif inp.sonars[2]>0.8:
                fwd=1
                rev=0
                nextState='search'
        # elif state=='search':
        #     while counterA>0:
        #         if inp.sonars[2]>0.8:
        #             fwd=1
        #             rev=0
        #             nextState=state
        #         elif 0.5<inp.sonars[2]<0.7 and 0.5<inp.sonars[4]<0.7 and 0.5<inp.sonars[0]<0.7:
        #             fwd=0
        #             rev=-1
        #             nextState='rotateToStationA'

        #         counterA-=1

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
