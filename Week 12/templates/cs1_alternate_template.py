from kivy.app import App 
from kivy.uix.label import Label  

class AlternateApp(App):
	
	def build(self):
		self.mytext=Label(text='Wei Jin --->', font_size=100)
		self.mytext.bind(on_touch_down=self.alternate)
		self.state=0
		return self.mytext

	def alternate(self,instance, touch):
		if self.state==0:
			self.mytext.text= "Wei Jin --->"
			self.state=1
		else:
			self.mytext.text= "<--- Shi Wei"
			self.state=0
		# self.state=1-self.state
		

myapp=AlternateApp() # obj instantiation
myapp.run() # event loop