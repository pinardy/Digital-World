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
    newRoute=['goStraight','goStraight']+newRoute+['stop'] #from the link
    # newRoute=['turnLeft','turnRight'] #arbitary test path
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
    startState={'state':'forward','pos':routes[0],'route':routes[1],'time':time.time(),'num':0,'previousAngle':0,'posNum':0,'preRightDistance':0,'outputText':'','desiredAngle':0}

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
        desiredAngle=state['desiredAngle']
        fvel=0.15
        rvel=0.0

        print data
        
        if currentState=='turnLeft':
            desiredAngle=state['previousAngle']+0.42*math.pi
            state['desiredAngle']=desiredAngle
        if currentState=='turnRight':
            desiredAngle=state['previousAngle']-0.4*math.pi
            state['desiredAngle']=desiredAngle
               
        if desiredAngle>2*math.pi:
            desiredAngle-=2*math.pi
        if desiredAngle<0:
            desiredAngle+=2*math.pi

        if currentState=='forward':
                                                
            if (data[0]>=2 and data[1]>=1.5) or (data[3]>=2 and data[4]>=1.5):
                output=io.Action(0.0, 0.0)
                state['state']='junction'

            #   obstacle 
            elif (data[2]<=0.5 or data[1]<=0.7) and data[3]>=0.8:
                output=io.Action(0.0,0.0)
                state['desiredAngle']=currentAngle-0.1*math.pi
                state['state']='leftObstacle'
            elif (data[2]<=0.5 or data[3]<=0.7) and data[1]>=0.8:
                output=io.Action(0.0,0.0)
                state['desiredAngle']=currentAngle+0.1*math.pi
                state['state']='rightObstacle'
            if  data[2]<=0.5 and data[1]<=0.8 and data[3]<=0.8 and data[0]<=0.8 and data[4]<=0.8:
                output=io.Action(0.0, 0.0)
                state['state']='wait'
                state['time']=time.time()

            else:
                if data[1]>=2 or data[3]>=2:
                    rvel=0    
                elif route[num]=='turnLeft':
                    rvel =-(29.77*state['preRightDistance']-30*(data[0]-0.67))
                    state['preRightDistance']=data[0]-0.67
                else:
                    rvel =29.77*state['preRightDistance']-30*(data[4]-0.67)
                    state['preRightDistance']=data[4]-0.67
                output=io.Action(fvel,rvel) 
                
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
                 outputText=time.strftime("<%H:%M:%S>||<%d-%b-%Y>", time.localtime())+outputText
                 state['outputText']+=outputText+'\n'
                 state['posNum']=posNum+1
                 output=io.Action(0.0,0.0)                      
                                                                                                
        if currentState=='turnRound':
                if data[2]>=2 and rightAngle>=leftAngle-0.8:
                        output=io.Action(fvel, 0.0)
                        state['state']='forward'  
                else:
                        output=io.Action(0.0, 0.2)
                        
        if currentState=='turnLeft':
                if desiredAngle<0.5*math.pi:
                    if currentAngle<=math.pi and currentAngle>=desiredAngle:
                        if data[0]<=1.2 and data[4]<=1.2 and data[2]>=2:
                            output=io.Action(fvel,0.0)
                            state['state']='forward'
                            state['num']=num+1 
                        else:
                            output=io.Action(fvel,0.0)
                    else:
                        output=io.Action(0.08, 0.2) #value was doubled
                else:
                    if currentAngle>=desiredAngle:
                        if data[0]<=1.2 and data[4]<=1.2 and data[2]>=2:
                            output=io.Action(fvel,0.0)
                            state['state']='forward'
                            state['num']=num+1 
                        else:
                            output=io.Action(fvel,0.0)
                    else:
                        output=io.Action(0.08, 0.2) #value was doubled 
            
                    
        if currentState=='turnRight':
                if desiredAngle<=0.5*math.pi:
                    print 1
                    if currentAngle<=desiredAngle:
                        if data[0]<=1.2 and data[4]<=1.2:
                            output=io.Action(fvel,0.0)
                            state['state']='forward'
                            state['num']=num+1  
                        else:
                            output=io.Action(fvel,0.0)
                    elif currentAngle>=6:
                        if data[0]<=1.2 and data[4]<=1.2 and data[2]>=2:
                            output=io.Action(fvel,0.0)
                            state['state']='forward'
                            state['num']=num+1  
                        else:
                            output=io.Action(fvel,0.0)
                    else:
                        output=io.Action(0.08, -0.2)
                elif desiredAngle>=1.5*math.pi:
                    print 2
                    if currentAngle<=desiredAngle and currentAngle>=math.pi:
                        if data[0]<=1.2 and data[4]<=1.2 and data[2]>=2:
                            output=io.Action(fvel,0.0)
                            state['state']='forward'
                            state['num']=num+1  
                        else:
                            output=io.Action(fvel,0.0)
                    else:
                        output=io.Action(0.08, -0.2)
                else:
                    print 3
                    if currentAngle<=desiredAngle:
                        if data[0]<=1.2 and data[4]<=1.2 and data[2]>=2:
                            output=io.Action(fvel,0.0)
                            state['state']='forward'
                            state['num']=num+1  
                        else:
                            output=io.Action(fvel,0.0)
                    else:
                        output=io.Action(0.08, -0.2)  
                         
        if currentState=='stop':
            output=io.Action(0.0,0.0)
            outputFile=open('outputFile.txt','w')
            outputText=time.strftime("<%H:%M:%S>||<%d-%b-%Y>", time.localtime())+'Finished, and arrived at X'
            state['outputText']+=outputText
            outputFile.write(state['outputText'])
            outputFile.close
            
        if currentState=='rightObstacle':
            if desiredAngle<0.5*math.pi:
                if currentAngle<=math.pi and currentAngle>=desiredAngle:
                    output=io.Action(fvel,0.0)
                    state['state']='followRight'
                else:
                    output=io.Action(0.05, 0.16) 
            else:
                if currentAngle>=desiredAngle:
                    output=io.Action(fvel,0.0)
                    state['state']='followRight'
                else:
                    output=io.Action(0.05, 0.16)
        if currentState=='followRight':
            if data[2]<=0.5 and data[0]<=0.5 and data[1]<=0.7:
                state['state']='wait'
                output=io.Action(0.0,0.0)
            elif data[0]>=0.5 and data[1]>=0.7:
                state['state']='junction'
                output=io.Action(0.0,0.0)
            elif data[3]>0.7:
                output=io.Action(0.12,0.0)
            else:
                rvel =(29.77*state['preRightDistance']-30*(data[4]-0.15))
                state['preRightDistance']=data[4]-0.15
                output=io.Action(0.1,rvel)
        
        if currentState=='leftObstacle':
            if desiredAngle<=0.4*math.pi: #initially 5
                if currentAngle<=desiredAngle+0.5:
                    output=io.Action(0.0,0.0)
                    state['state']='followLeft'
                elif currentAngle>=5: #initially 6
                    output=io.Action(0.0,0.0)
                    state['state']='followLeft'
                else:
                    output=io.Action(0.05, -0.16)
            elif desiredAngle>=1.5*math.pi:
                if currentAngle<=desiredAngle and currentAngle>=math.pi:
                    output=io.Action(0.0,0.0)
                    state['state']='followLeft'
                else:
                    output=io.Action(0.05, -0.16)
            else:
                if currentAngle<=desiredAngle+0.5:
                    output=io.Action(0.0,0.0)
                    state['state']='followLeft'
                else:
                    output=io.Action(0.06, -0.16)  
            
        if currentState=='followLeft':
            if data[2]<=0.5 and data[4]<=0.5 and data[3]<=0.7:
                output=io.Action(0.0,0.0)
                state['state']='wait'
            elif data[0]>=0.5 and data[3]>=0.7:
                state['state']='junction'
                output=io.Action(0.0,0.0)
            elif data[1]>0.7:
                output=io.Action(0.12,0.0)
            else:
                rvel=-(29.77*state['preRightDistance']-30*(data[0]-0.15))
                state['preRightDistance']=data[0]-0.15
                output=io.Action(0.1,rvel)
                                                     
        print currentState
        print currentAngle
        print desiredAngle
        print fvel,rvel
        #print route
        #print 'next station: '+pos[posNum]

        return (state, output)

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
