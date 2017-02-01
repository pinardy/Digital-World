# Import eBot and time module
from eBot import eBot
from time import sleep

def forward(speed, duration):
    ebot.wheels(speed, speed)
    sleep(duration)
    #ebot.halt  P.S. Do not use ebot.halt() to disconnect from the eBot,
    #as it will only disable the motors and LEDs without disconnecting 
    #from the robot. 
    ebot.disconnect()

ebot = eBot.eBot() # create an eBot object
ebot.connect() # connect to the eBot via Bluetooth

############### Start writing your code here ################ 
speed = float(raw_input('What do you want the speed of the ebot to be: '))
duration = float(raw_input('How long do u want the ebot to run for in seconds: '))
forward(speed, duration)

ebot.temperature()
TempC = ebot.temperature()
print "Temperature in Celsius is %.3f" %TempC
TempF = (TempC)*float(9)/5+32
print "Temperature in Fahrenheit is %.3f" %TempF
#ebot.imperial_march()
ebot.disconnect() # disconnect the Bluetooth communication
########################## end ############################## 

 # disconnect the Bluetooth communication
