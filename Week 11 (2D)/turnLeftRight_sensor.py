	if currentState=='turnRight': # Uses sensors instead of odometry
            if data[3]>=1.5 or data[4]>=1 and data[2]<=2: #if turn too much at corner
                output=io.Action(0.08,-0.16)
                state['state']='turnRight'
            elif data[3]<=1 or data[4]<=1.5 and data[2]>=2: #for ideal turn
                output=io.Action(0.13,0)
                state['state']='forward'
                state['num']=num+1
            else:
                output=io.Action(0.068,-0.13)
                state['state']='turnRight'

    if currentState=='turnLeft': # Uses sensors instead of odometry
            if data[1]>=1.5 or data[0]>=1 and data[2]<=2: #if turn too much at corner
                output=io.Action(0.08, 0.16)
                state['state']='turnLeft'
            elif data[1]<=1.5 or data[0]<=1.0 and data[2]>=2: #for ideal turn
                output=io.Action(0.13,0)
                state['state']='forward'
                state['num']=num+1
            else:
                output=io.Action(0.068,0.13)