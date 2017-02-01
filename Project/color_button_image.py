from kivy.app import App 
from kivy.uix.label import Label  

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.app import App
from kivy.uix.image import Image
# import kivy

class AlternateApp(App):

	def build(self):
                    self.layout=BoxLayout()
                    self.settings=Button(text='Settings',color=(0,1,0,0.8),on_press=self.detect,size_hint = (1, 0.3), 
                    background_color = [1, 0, 0, 1])  
        # color=(0,1,0,0.8) means the word, Settings, is green in color and 80% opaque
        # size_hint = (1, 0.3) means  the button occupies 100% of the x-axis and 30% of the y-axis
        # background_color = [1,0,0,1] means the button is red in color and 100% opaque
                    self.layout.add_widget(self.settings)
                    self.quit=Button(text='Quit',on_press=self.detect)
                    self.layout.add_widget(self.quit)
                    wag = Image(source='c:/Pinardy/SUTD/Digital World/cohort_classroom.jpg',pos_hint={'center_x': 0, 'center_y': 0.5})
        # add image smiley.jpg and the position is at the center
                    self.layout.add_widget(wag)
	            return self.layout

	def detect(self,instance):  
                    print 'You have clicked me!'

AlternateApp().run()