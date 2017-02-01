import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io
import time
import firebase
import urllib2

def getRoute(f):
    lines=f.readlines()
    goal={}
    route=['X']
    newRoute=[]
    for i in lines:
        x=[]
        x+=i.split()
        goal[x[0]]=x[1]
    print goal
    for n in sorted(goal.keys()):
        route+=([n]+['X'])*((int(goal[n])-1)/6+1)
    for m in range(len(route)-1):
        if route[m]=='X':
            if route[m+1]=='A':
                newRoute+=['turnRight','turnRight','turnLeft','turnLeft']
            elif route[m+1]=='B':
                newRoute+=['turnRight','goStraight','goStraight','turnLeft']
            elif route[m+1]=='C':
                newRoute+=['goStraight','turnRight','goStraight','goStraight','turnLeft','goStraight']
            elif route[m+1]=='D':
                newRoute+=['goStraight','turnRight','turnLeft','turnRight','turnLeft','goStraight']
    newRoute=['goStraight','goStraight']+newRoute+['stop']
    
    return route,newRoute
 
url = "https://gintaka.firebaseio.com/" 
token = "74Dm9anUkDBN91Wb2O39FWdch5d2JcH9yBMLSpqB" 
firebase = firebase.FirebaseApplication(url, token)   
    
req = urllib2.Request('http://people.sutd.edu.sg/~oka_kurniawan/10_009/y2015/2d/tests/level2_2.inp')
req.add_header('User-agent', 'SUTD 2D Demo')
inputFile = urllib2.urlopen(req)
routes=getRoute(inputFile)
print routes

class MySMClass(sm.SM):
    startState={'state':'forward','pos':routes[0],'route':routes[1],'time':time.time(),'num':0,'previousAngle':0,'posNum':0,'preRightDistance':0}

    def getNextValues(self, state, inp):
        
        data = inp.sonars
        an = inp.analogInputs
        od = inp.odometry
        temp = inp.temperature
        ldr = inp.light
        leftAngle=float(data[1])/float(data[0])
        rightAngle=float(data[3])/float(data[4])
        outputFile=open('outputFile.txt','w')   
        currentState=state['state']
        route=state['route']
        pos=state['pos']
        previousTime=state['time']
        num=state['num']
        posNum=state['posNum']
        currentAngle=od.theta
        desiredAngle=0
        fvel=0.13
        
        print data
        
        if currentState=='turnRound':
            desiredAngle=state['previousAngle']+math.pi
        if currentState=='turnLeft':
            desiredAngle=state['previousAngle']+0.5*math.pi
        if currentState=='turnRight':
            desiredAngle=state['previousAngle']-0.5*math.pi
               
        if desiredAngle>2*math.pi:
            desiredAngle-=2*math.pi
        if desiredAngle<0:
            desiredAngle+=2*math.pi

        if currentState=='forward':
            
            #if  0.72<=data[2]<=0.80 and 0.8<=data[1]<=0.88 and 0.8<=data[3]<=0.88 and 0.8<=data[0]<=0.88 and 0.8<=data[4]<=0.88:
            #    output=io.Action(0.03, 0.0)
            #    state['state']='forward'
            #elif  data[2]<=0.65 and data[1]<=0.86 and data[3]<=0.86 and data[0]<=0.86 and data[4]<=0.86:
            #    output=io.Action(0.042, 0.0)
            #    state['state']='forward'
            #elif  data[2]<=0.55 and data[1]<=0.82 and data[3]<=0.82 and data[0]<=0.82 and data[4]<=0.82:
            #    output=io.Action(0.017, 0.0)
            #    state['state']='forward'                                         
            if  data[2]<=0.5 and data[1]<=0.8 and data[3]<=0.8 and data[0]<=0.8 and data[4]<=0.8:
                output=io.Action(0.0, 0.0)
                state['state']='wait'
                state['time']=time.time()
            #elif data[2]<=0.85:
            #    output=io.Action(0.03,0)
            #    state['state']='forward'
                fvel=0.065*(data[2]-0.5)
            elif (data[0]>=2 and data[1]>=1.5) or (data[3]>=2 and data[4]>=1.5):
                output=io.Action(fvel, 0.0)
                state['state']='junction'
            #elif data[3]>=2:
            #    output=io.Action(fvel,0.0)
            else:
                if route[num]=='turnLeft':
                    rvel =-(29.77*state['preRightDistance']-30*(data[0]-0.67))
                    state['preRightDistance']=data[0]-0.67
                elif route[num]=='goStraight' and (data[1]>=2 or data[3]>=2):
                    rvel=0
                else:
                    rvel =29.77*state['preRightDistance']-30*(data[4]-0.67)
                    state['preRightDistance']=data[4]-0.67
                #if data[1]>=2 or data[3]>=2:
                #    if rvel>=0.35:
                #        rvel=0.35
                #    if rvel<=-0.35:
                #        rvel=-0.35
                output=io.Action(fvel,rvel) 
                
                #2
                #if route[num]=='turnLeft':
                #    rvel =-(29.77*state['preRightDistance']-30*(data[0]-0.67))
                #    state['preRightDistance']=data[0]-0.67
                #elif route[num]=='goStraight' and (data[1]>=2 or data[3]>=2):
                #    rvel=0
                #else:
                #    rvel =29.45*state['preRightDistance']-30*(data[4]-0.67)
                #    state['preRightDistance']=data[4]-0.67
                #if rvel>=0.35:
                #    rvel=0.35
                #if rvel<=-0.35:
                #    rvel=-0.35
                #output=io.Action(fvel,rvel)    
                #1
                #rvel =29.77*state['preRightDistance']-30*(data[4]-0.67)
                #state['preRightDistance']=data[4]-0.67
                #if rvel>=0.3:
                #    rvel=0.3
                #elif rvel<=-0.3:
                #    rvel=-0.3
                #output=io.Action(fvel, rvel)
              
        if currentState=='junction':
                    state['state']=route[num]
                    output=io.Action(fvel,0.0)
                    state['previousAngle']=currentAngle
                    
        if currentState=='goStraight':
            if data[0]<=2 and data[4]<=2:
                output=io.Action(fvel, 0.0)
                state['state']='forward'
                state['num']=num+1 
            else:
                 output=io.Action(fvel, 0.0)  
        
        if currentState=='wait':
            if time.time()<=previousTime+5:                    
                 output=io.Action(0.0,0.0)
            else:
                 state['state']='turnRound'
                 outputTime=time.strftime("%H:%M:%S|%d/%b/%Y", time.localtime())
                 firebase.put('/','Station'+pos[posNum]+'/ldr',ldr[0])
                 firebase.put('/','Station'+pos[posNum]+'/temp',temp)
                 firebase.put('/','Station'+pos[posNum]+'/time',outputTime)
                 if posNum==len(pos):
                     state['state']='stop'
                 if pos[posNum]=='X':
                     outputText='Collect Plates at X'
                 else:
                     outputText='Expose Plates at' +pos[posNum]
                 outputFile=open('outputFile.txt','w')
                 outputText=time.strftime("<%H:%M:%S>||<%d-%b-%Y>", time.localtime())+outputText
                 outputFile.write(outputText)
                 outputFile.close
                 state['posNum']=posNum+1
                 output=io.Action(0.0,0.0)                      
                                                                                                
        if currentState=='turnRound':
                if data[2]>=2 and rightAngle>=leftAngle-0.1:
                #if desiredAngle>=math.pi:
                #    if currentAngle>=desiredAngle:
                #        output=io.Action(fvel, 0.0)
                #        state['state']='forward'
                #        state['num']=num+1  
                #    else:
                #        output=io.Action(0.0, 0.2)
                #else:
                #    if currentAngle>=desiredAngle and currentAngle<=math.pi:
                        output=io.Action(fvel, 0.0)
                        state['state']='forward'
                        #state['num']=num+1  
                else:
                        output=io.Action(0.0, 0.16)
                        
        if currentState=='turnLeft':
                #if data[3]<=1.2 and data[4]<=0.9:
                #    output=io.Action(0.1,0.2)
                #    state['state']='turnLeft' 
                #if data[0]<=0.1 and data[1]<=1.2:
                #    output=io.Action(0.05,0.12)
                #    state['state']='turnLeft'           
                if desiredAngle<0.5*math.pi:
                    if currentAngle<=math.pi and currentAngle>=desiredAngle:
                        if data[0]<=1.2 and data[4]<=1.2 and data[2]>=2:
                            output=io.Action(0.13,0.0)
                            state['state']='forward'
                            state['num']=num+1 
                        else:
                            output=io.Action(0.13,0.0)
                    else:
                        output=io.Action(0.065, 0.16)
                else:
                    if currentAngle>=desiredAngle:
                        if data[0]<=1.2 and data[4]<=1.2 and data[2]>=2:
                            output=io.Action(0.13,0.0)
                            state['state']='forward'
                            state['num']=num+1 
                        else:
                            output=io.Action(0.13,0.0)
                    else:
                        output=io.Action(0.065, 0.16) 
            
                    
        if currentState=='turnRight':
                #if data[0]<=1.2 and data[1]<=0.9:
                #    output=io.Action(0.1,-0.2)
                #    state['state']='turnRight'
                if desiredAngle<=0.5*math.pi:
                    print 1
                    if currentAngle<=desiredAngle:
                        if data[0]<=1.2 and data[4]<=1.2:
                        #and data[2]>=2:
                            output=io.Action(0.13,0.0)
                            state['state']='forward'
                            state['num']=num+1  
                        else:
                            output=io.Action(0.13,0.0)
                    elif currentAngle>=6:
                        if data[0]<=1.2 and data[4]<=1.2 and data[2]>=2:
                            output=io.Action(0.13,0.0)
                            state['state']='forward'
                            state['num']=num+1  
                        else:
                            output=io.Action(0.13,0.0)
                    else:
                        output=io.Action(0.065, -0.16)
                elif desiredAngle>=1.5*math.pi:
                    print 2
                    if currentAngle<=desiredAngle and currentAngle>=math.pi:
                        if data[0]<=1.2 and data[4]<=1.2 and data[2]>=2:
                            output=io.Action(0.13,0.0)
                            state['state']='forward'
                            state['num']=num+1  
                        else:
                            output=io.Action(0.13,0.0)
                    #elif currentAngle<=0.0075:
                    #    output=io.Action(0.13,0.0)
                    else:
                        output=io.Action(0.065, -0.16)
                else:
                    print 3
                    if currentAngle<=desiredAngle:
                        if data[0]<=1.2 and data[4]<=1.2 and data[2]>=2:
                            output=io.Action(0.13,0.0)
                            state['state']='forward'
                            state['num']=num+1  
                        else:
                            output=io.Action(0.13,0.0)
                    else:
                        output=io.Action(0.08, -0.2)  
                         
        if currentState=='stop':
            output=io.Action(0.0,0.0)
            outputFile=('outputFile.txt','w')
            outputText=time.strftime("<%H:%M:%S>||<%d-%b-%Y>", time.localtime())+'Finished, and arrived at X'
            outputFile.write(outputText)
            outputFile.close
            
        print currentState
        print currentAngle
        print desiredAngle
        print fvel,rvel
        print route
        print 'next station: '+pos[posNum]
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
