import time
import firebase
url = "https://elainejomane.firebaseio.com/" # URL to Firebase database
token = "D68F25AuafW6vMWNHGx4iYTzL68rJw2AAiJ9QCOI" # unique token used for authentication
firebase = firebase.FirebaseApplication(url, token)
t = 0
while True:
    t += 1
    time.sleep(0.01)
    clr1c = firebase.get('/clr1c')
    clr1o = firebase.get('/clr1o')
    clr1 = firebase.get('/clr1')
    if (clr1c+clr1o)== 0 and clr1 != 2:
        firebase.put('/','clr1', 0) 
    if (clr1c+clr1o) > 0 and clr1 != 2:
        firebase.put('/','clr1', 1)
    print "I is working", t