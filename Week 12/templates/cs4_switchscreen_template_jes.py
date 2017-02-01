from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout=BoxLayout()
        btn1 = Button(text="Settings", on_press=self.changeToSetting)
        btn2 = Button(text="Quit", on_press=self.quitApp)
        self.layout.add_widget(btn1)
        self.layout.add_widget(btn2)
        self.add_widget(self.layout)
		
    def changeToSetting(self, value):
        self.manager.transition.direction = 'left'
        # modify the current screen to a different "name"
    	self.manager.current = 'settings'

    def quitApp(self, value):
        App.get_running_app().stop()


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout=BoxLayout()
        btn1 = Button(text="Back To Menu", on_press=self.changeToMenu)
        self.layout.add_widget(Label(text="Settings Screen",font_size=50))
        self.layout.add_widget(btn1)
        self.add_widget(self.layout)

    def changeToMenu(self,value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
        self.manager.current= 'menu'



class SwitchScreenApp(App):
	def build(self):
            sm=ScreenManager()
            ms=MenuScreen(name='menu')
            st=SettingsScreen(name='settings')
            sm.add_widget(ms)
            sm.add_widget(st)
            sm.current='menu'
            return sm

if __name__=='__main__':
	SwitchScreenApp().run()
