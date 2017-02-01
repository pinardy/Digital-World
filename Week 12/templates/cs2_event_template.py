from kivy.app import App
from kivy.uix.label import Label 

class SlideDetectApp(App):
	def build(self):
		self.mytext=Label(text='Slide me', font_size=100)
		self.mytext.bind(on_touch_move=self.detect)
		return self.mytext

	def detect(self, instance, touch):
		# if not instance.collide_point(touch.x, touch.y):
		# 	return False
		if touch.dx<-40:
			self.mytext.text= "Slide left"
			# self.mytext.font_size=20
		if touch.dx>40:
			self.mytext.text= "Slide right"
			# self.mytext.font_size=40
		if touch.dy<-40:
			self.mytext.text= "Slide down"
			# self.mytext.font_size=60
		if touch.dy>40:
			self.mytext.text= "Slide up"
			# self.mytext.font_size=80
		return True

if __name__=='__main__':
	SlideDetectApp().run()