import firebase
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton 

url = "https://pinardy.firebaseio.com/" 
token = "4vlssuGd2ljBfQSy07CKFIqhEIpd7LcFMunm6Jmj" 
firebase = firebase.FirebaseApplication(url, token) 

class GuiKivy(App):

	def build(self):
		layout=GridLayout(cols=2)
		
		layout.add_widget(Label(text="Yellow LED", halign='left'))
		self.btnYellow = Button(text="Turn ON", on_press=self.yellowtoggle, halign = 'left')
       	        layout.add_widget(self.btnYellow)

           	layout.add_widget(Label(text="Red LED", halign='left'))
		self.btnRed = Button(text="Turn ON", on_press=self.redtoggle, halign = 'left')
               	layout.add_widget(self.btnRed)
                
                self.red = firebase.get('/red')
                self.yellow = firebase.get('/yellow')    
                
           	if self.red == 0:
                    self.btnRed.text = "Turn ON"
                elif self.red == 1:
                    self.btnRed.text = "Turn OFF"
                if self.red == None:
                    self.btnRed.text = "Turn ON"
                    self.red = 0
            
                if self.yellow == 0:
                    self.btnYellow.text = "Turn ON"
                elif self.yellow == 1:
                    self.btnYellow.text = "Turn OFF"
                elif self.yellow == None:
                    self.btnYellow.text = "Turn ON"
                    self.yellow = 0

		return layout

	def yellowtoggle(self, instance):
		 self.yellow = 1-self.yellow
		 firebase.put('/','yellow',self.yellow)
                 if self.yellow == 0:
                     self.btnYellow.text = "Turn ON"
                 elif self.yellow == 1:
                     self.btnYellow.text = "Turn OFF"

        def redtoggle(self, instance):
 		 self.red = 1-self.red
 		 firebase.put('/','red',self.red)
                 if self.red == 0:
                     self.btnRed.text = "Turn ON"
                 elif self.red == 1:
                     self.btnRed.text = "Turn OFF"

GuiKivy().run()

