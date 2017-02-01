import RPi.GPIO as GPIO
import time
import firebase

url = "https://pinardy.firebaseio.com/" 
token = "4vlssuGd2ljBfQSy07CKFIqhEIpd7LcFMunm6Jmj" 
firebase = firebase.FirebaseApplication(url, token) 

sensor = 4
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
 
previous_state = False
current_state = False
lights_on = False
ptimer = 0
 
while True:
    time.sleep(0.001)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state == 0:
        ptimer += 0.001
    else: ptimer = 1
    if ptimer > 5 and lights_on == False:
        lights_on = False
        print "LIGHTS OFF"
        firebase.put('/','Demoroom_Alpha',{'occupied': 0})

    if current_state == 1 and lights_on == True:
        lights_on = True
        print "LIGHTS ON"
        firebase.put('/','Demoroom_Alpha',{'occupied': 1})
    print "Lights", lights_on
    print "PTimer", ptimer