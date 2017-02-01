import firebase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

url = "https://pinardy.firebaseio.com/" 
token = "4vlssuGd2ljBfQSy07CKFIqhEIpd7LcFMunm6Jmj" 
firebase = firebase.FirebaseApplication(url, token) 

class lightLED(App): 

	def build(self):
		layout= GridLayout(cols=2)

		layout.add_widget(Label(text="Yellow LED", halign='left'))
		btnYellow = ToggleButton(text="Off", on_press=self.calculate)
		layout.add_widget(btnYellow)

		layout.add_widget(Label(text="Red LED", halign='left'))
		btnRed = ToggleButton(text="Off", on_press=self.calculate)
		layout.add_widget(btnRed)

lightLED().run()

