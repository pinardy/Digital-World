import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io
import time
import firebase

# def getRoute(f):
#     lines=f.readlines()
#     goal={}
#     route=['X']
#     newRoute=[]
#     for i in lines:
#         x=[]
#         x+=i.split()
#         goal[x[0]]=x[1]
#     print goal
#     for n in sorted(goal.keys()):
#         route+=([n]+['X'])*((int(goal[n])-1)/6+1)
#     for m in range(len(route)-1):
#         if route[m]=='X':
#             if route[m+1]=='A':
#                 newRoute+=['turnRound','turnRight','turnRight','turnRound','turnLeft','turnLeft']
#             elif route[m+1]=='B':
#                 newRoute+=['turnRound','turnRight','goStraight','turnRound','goStraight','turnLeft']
#             elif route[m+1]=='C':
#                 newRoute+=['turnRound','goStraight','turnRight','goStraight','turnRound','goStraight','turnLeft','goStraight']
#             elif route[m+1]=='D':
#                 newRoute+=['turnRound','goStraight','turnRight','turnLeft','turnRound','turnRight','turnLeft','goStraight']
# #?newRoute=['goStraight','goStraight']+newRoute+['stop']
#     newRoute=newRoute+['stop']
#     return route,newRoute
 
url = "https://gintaka.firebaseio.com/" 
token = "74Dm9anUkDBN91Wb2O39FWdch5d2JcH9yBMLSpqB" 
firebase = firebase.FirebaseApplication(url, token)   
    
# inputFile=open('level2_1.inp','r')
# routes=getRoute(inputFile)
routes=[0,['turnRound','turnRight','turnRight','turnRound','turnLeft','turnLeft']]
print routes

class MySMClass(sm.SM):
    startState={'state':'forward','pos':routes[0],'route':routes[1],'time':time.time(),'num':0,'previousAngle':0,'posNum':0}

    def getNextValues(self, state, inp):
        
        data = inp.sonars
        an = inp.analogInputs
        od = inp.odometry
        temp = inp.temperature
        ldr = inp.light
        #leftAngle=float(data[1])/float(data[0])
        #rightAngle=float(data[3])/float(data[4])
        outputFile=open('outputFile.txt','w')   
        currentState=state['state']
        route=state['route']
        pos=state['pos']
        previousTime=state['time']
        num=state['num']
        posNum=state['posNum']
        currentAngle=od.theta
        desiredAngle=0
        fvel=0.15
        alignr=data[3]*math.cos(math.pi/4.0)
        alignl=data[1]*math.cos(math.pi/4.0)
                
        if currentState=='turnRound':
            desiredAngle=state['previousAngle']+3
        if currentState=='turnLeft':
            desiredAngle=state['previousAngle']+1.5
        if currentState=='turnRight':
            desiredAngle=state['previousAngle']-1.5
               
        if desiredAngle>2*math.pi:
            desiredAngle-=2*math.pi
        if desiredAngle<0:
            desiredAngle+=2*math.pi

        if currentState=='forward':
            if data[2]<=0.8 and data[1]<=2 and data[3]<=2:
                output=io.Action(0.0, 0.0)
                state['state']='junction'
                state['time']=time.time()
            elif (alignr<data[4] and data[4]<0.72)or data[4]<0.7:
                state['state']='forward'
                output=io.Action(0.08,0.05)
            elif (alignl<data[0] and data[0]<0.72)or data[0]<0.7:
                state['state']='forward'
                output=io.Action(0.08,-0.05)
            #---- 2nd layer of controller ----#
            elif (alignr<data[4] and data[4]<0.5)or data[4]<0.5:
                state['state']='forward'
                output=io.Action(0.08,0.10)
            elif (alignl<data[0] and data[0]<0.5)or data[0]<0.5:
                state['state']='forward'
                output=io.Action(0.08,-0.1)
            #---- 2nd layer of controller ----#  
            elif data[1]==data[3] and data[0]==data[4]:
                 output=io.Action(0.15,0)
                 state['state']='forward'              
            elif (data[0]>=2 or data[4]>=2) and (data[1]>=2 or data[3]>=2):
                output=io.Action(fvel, 0.0)
                state['state']='junction'
            else:
                output=io.Action(fvel, 0.0)
                state['state']='forward'
        #       
        if currentState=='junction':
                if route[num]=='turnRound':
                    state['state']=route[num]
                    output=io.Action(fvel,0.0)
                    state['previousAngle']=currentAngle
                    state['time']=time.time()
                    outputTime=time.strftime("%H:%M:%S|%d/%b/%Y", time.gmtime())
                    firebase.put('/','Station'+pos[posNum]+'/ldr',ldr[0])
                    firebase.put('/','Station'+pos[posNum]+'/temp',temp)
                    firebase.put('/','Station'+pos[posNum]+'/time',outputTime)
                    if pos[posNum]=='X':
                        outputText='Collect Plates at X'
                    else:
                        outputText='Expose Plates at' +pos[posNum]
                    outputText=time.strftime("<%H:%M:%S>||<%d-%b-%Y>", time.gmtime())+outputText
                    outputFile.write(outputText)
                    state['posNum']=posNum+1
                else:
                    state['state']=route[num]
                    output=io.Action(fvel,0.0)
                    state['previousAngle']=currentAngle
        if currentState=='goStraight':

            if data[0]<=2 and data[4]<=2:
                output=io.Action(fvel, 0.0)
                state['state']='forward'
                state['num']=num+1 

            if data[3]>=2 and data[4]<3:
                output=io.Action(0.0,-1.0)
                state['state']='turnRight'
                state['num']=num+1 
            else:
                 output=io.Action(fvel, 0.0)             
        if currentState=='turnRound':
            if time.time()<=previousTime+8:
                output=io.Action(0.0, 0.0)
            else:
                if desiredAngle>=math.pi:
                    if currentAngle>=desiredAngle:
                        output=io.Action(fvel, 0.0)
                        state['state']='forward'
                        state['num']=num+1  
                    else:
                        output=io.Action(0.0, 0.2)
                else:
                    if currentAngle>=desiredAngle and currentAngle<=math.pi:
                        output=io.Action(fvel, 0.0)
                        state['state']='forward'
                        state['num']=num+1  
                    else:
                        output=io.Action(0.0, 0.2)
        if currentState=='turnLeft':
            if desiredAngle<0.5*math.pi :
                # if currentAngle<=math.pi and currentAngle>=desiredAngle:
                if data[0]<=2 and data[1]<=2 and data[2]>=2.5:
                    output=io.Action(fvel,0.0)
                    state['state']='forward'
                    state['num']=num+1 
                else:
                    output=io.Action(0.1, 0.128)
            else:
                if currentAngle>=desiredAngle:
                    output=io.Action(fvel,0.0)
                    state['state']='forward'
                    state['num']=num+1
                else:
                    output=io.Action(0.1, 0.128)
        if currentState=='turnRight':
            if data[3]<=2 and data[4]<=2 and data[2]>=2.5:
                output=io.Action(fvel,0.0)
                state['state']='forward'
                state['num']=num+1 
            else:
                output=io.Action(0.1,-0.15)
            #if desiredAngle<=0.5*math.pi:
            #    if currentAngle<=desiredAngle:
            #        output=io.Action(fvel,0.0)
            #        state['state']='forward'
            #        state['num']=num+1 
            #    elif currentAngle>=6:
            #        output=io.Action(fvel,0.0)
            #        state['state']='forward'
            #        state['num']=num+1 
            #    else:
            #        output=io.Action(0.1, -0.15)
            #if desiredAngle>=1.5*math.pi:
            #    if currentAngle>=desiredAngle:
            #        output=io.Action(fvel,0.0)
            #        state['state']='forward'
            #        state['num']=num+1 
            #    elif currentAngle<=0.0075:
            #        output=io.Action(fvel,0.0)
            #        state['state']='forward'
            #        state['num']=num+1 
            #    else:
            #        output=io.Action(0.1, -0.15)
            #else:
            #    if currentAngle<=desiredAngle:
            #        output=io.Action(fvel,0.0)
            #        state['state']='forward'
            #        state['num']=num+1 
            #    elif currentAngle>=6:
            #        output=io.Action(fvel,0.0)
            #        state['state']='forward'
            #        state['num']=num+1 
            #    else:
            #        output=io.Action(0.1, -0.15)
        if currentState=='stop':
            output=io.Action(0.0,0.0)
            outputText=time.strftime("<%H:%M:%S>||<%d-%b-%Y>", time.gmtime())+'Finished, and arrived at X'
            outputFile.write(outputText)
            outputFile.close
            
        print state
        print currentState
        print currentAngle
        print desiredAngle
        #print rightAngle,leftAngle
        #print od.theta
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
                                  sonarMonitor=True) # sonar monitor widget
    
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
