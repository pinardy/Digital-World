# Import eBot and time module
from eBot import eBot
from time import sleep

def forward(speed, duration):
    speed = raw_input("""Enter the speed of robot in terms of decimals. For example, 50% throttle
    would mean that the speed is 0.5""")
    duration = raw_input("Enter the time of movement of robot in seconds: ")

    pass

ebot = eBot.eBot() # create an eBot object
ebot.connect() # connect to the eBot via Bluetooth

############### Start writing your code here ################ 

ebot.wheels(1, 1) # make the robot move at 100% speed on both wheels



########################## end ############################## 

ebot.disconnect() # disconnect the Bluetooth communication
