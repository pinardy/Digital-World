from RPi import GPIO
import firebase

url = "https://pinardy.firebaseio.com/" 
token = "4vlssuGd2ljBfQSy07CKFIqhEIpd7LcFMunm6Jmj" 
firebase=firebase.FirebaseApplication(url,token)

GPIO.setmode(GPIO.BCM)
ledcolor={'yellow':20, 'red':21}

GPIO.setup(ledcolor.values(), GPIO.OUT)

def setLED(ledno, status):
    if status == 0:
        GPIO.output(ledno, GPIO.LOW)
    elif status == 1:
        GPIO.output(ledno, GPIO.HIGH)


while True:
    time.wait(0.001)
    red = firebase.get('/red')
    yellow = firebase.get('/yellow')
    setLED(21,red) # value will be 0 or 1
    setLED(20,yellow) # value will be 0 or 1

######
while True:
    if GPIO.input(switch) == GPIO.HIGH: # switch is connected
        GPIO.output(led, GPIO.HIGH) # turn on the LED
    else: # switch is disconnected
        GPIO.output(led, GPIO.LOW) # turn off the LED
