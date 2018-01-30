from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.clock import Clock

import firebase
url = "https://pinardy.firebaseio.com/" # URL to Firebase database
token = "" # unique token used for authentication
firebase = firebase.FirebaseApplication(url, token)

            
class MainScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout=GridLayout(cols=2)
        # Add your code below to add the two Buttons
        bcls = Button(text="Classrooms", on_press=self.changeToClass, halign = 'left',font_size = 30)
        self.layout.add_widget(bcls)
        bmet = Button(text="Meeting Rooms", on_press=self.changeToMeeting, halign = 'left',font_size = 30)
        self.layout.add_widget(bmet)
        blib = Button(text="Library", on_press=self.changeToLibrary, halign = 'left',font_size = 30)
        self.layout.add_widget(blib)

        btn = Button(text="Quit", on_press=self.quitApp, halign = 'left',font_size = 30)
        self.layout.add_widget(btn)
        self.add_widget(self.layout)
        
    
    def changeToClass(self, value):
        self.manager.transition.direction = 'left'
        # modify the current screen to a different "name"
    	self.manager.current= 'classrooms'
    def changeToMeeting(self, value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
    	self.manager.current= 'meetingrooms'
    def changeToLibrary(self, value):
        self.manager.transition.direction = 'down'
        # modify the current screen to a different "name"
    	self.manager.current= 'library'
    
    def quitApp(self, value):
        App.get_running_app().stop()

class ClassroomScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout=GridLayout(cols=2)
        # Add your code below to add the two Buttons
        self.cr1t = Label(text="Classroom 1", halign = 'left',font_size = 30)
        self.layout.add_widget(self.cr1t)
        self.cr1b = Button(text="Book", on_press=self.book1, halign = 'left',font_size = 30)
        self.layout.add_widget(self.cr1b)
        
        self.cr2t = Label(text="Classroom 2", halign = 'left',font_size = 30)
        self.layout.add_widget(self.cr2t)
        self.cr2b = Button(text="Book", on_press=self.book2, halign = 'left',font_size = 30)
        self.layout.add_widget(self.cr2b)

        rf = Button(text = "Refresh", on_press = self.refresh, halign = 'left',font_size = 30)
        self.layout.add_widget(rf)
        bmn = Button(text="Back to Main", on_press=self.changeToMain, halign = 'left',font_size = 30)
        self.layout.add_widget(bmn)
        bmet = Button(text="Meeting Rooms", on_press=self.changeToMeeting, halign = 'left',font_size = 30)
        self.layout.add_widget(bmet)
        blib = Button(text="Library", on_press=self.changeToLibrary, halign = 'left',font_size = 30)
        self.layout.add_widget(blib)

        self.clr1 = firebase.get('/clr1')
        self.clr2 = firebase.get('/clr2')
        if self.clr1 == 0:
            self.cr1b.disabled = False
            self.cr1b.text = "Book"
        elif self.clr1 == 1:
            self.cr1b.disabled = True
            self.cr1b.text = "Cannot Book \n Room Occupied"
        elif self.clr1 == 2:
            self.cr1b.disabled = True
            self.cr1b.text = "Cannot Book \n Room Already Booked"
        else:
            self.cr1b.disabled = False
            self.clr1 = 0
        if self.clr2 == 0:
            self.cr2b.disabled = False
        elif self.clr2 == 1:
            self.cr2b.disabled = True
        elif self.clr2 == 2:
            self.cr2b.disabled = True
        else:
            self.cr2b.disabled = False
            self.clr2 = 0
            self.cr1b.text = "Book"
        
                
            
        btn = Button(text="Quit", on_press=self.quitApp, halign = 'left',font_size = 30)
        self.layout.add_widget(btn)
        self.add_widget(self.layout)
        
    def refresh(self,value):
        print "REFRESHING"
        self.clr1 = firebase.get('/clr1')
        self.clr2 = firebase.get('/clr2')
        if self.clr1 == 0:
            self.cr1b.disabled = False
            self.cr1b.text = "Book"
        elif self.clr1 == 1:
            self.cr1b.disabled = True
            self.cr1b.text = "Cannot Book \n Room Occupied"
        elif self.clr1 == 2:
            self.cr1b.disabled = True
            self.cr1b.text = "Cannot Book \n Room Already Booked"
        elif self.clr1 == None:
            self.cr1b.disabled = False
            self.clr1 = 0
            self.cr1b.text = "Book"
    
                
    def book1(self,value):
        if self.clr1 == 0:
            self.clr1 = 2
            self.cr1b.disabled = True
            self.cr1b.text = "Cannot Book \n Room Already Booked"
            firebase.put('/','clr1',self.clr1) 
        elif self.clr1 == 1:
            self.cr1b.disabled = True
        elif self.clr1 == 2:
            self.cr1b.disabled = True
        else:
            self.cr1b.disabled = False
            self.clr1 = 0
    def book2(self,value):
        if self.clr2 == 0:
            self.clr2 = 2
            self.cr2b.disabled = True
            firebase.put('/','clr2',self.clr2) 
        elif self.clr2 == 1:
            self.cr2b.disabled = True
        elif self.clr2 == 2:
            self.cr1b.disabled = True
        else:
            self.cr2b.disabled = False
            self.clr2 = 0
                
    def changeToMain(self, value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
    	self.manager.current= 'main'
    def changeToMeeting(self, value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
    	self.manager.current= 'meetingrooms'
    def changeToLibrary(self, value):
        self.manager.transition.direction = 'down'
        # modify the current screen to a different "name"
    	self.manager.current= 'library'
        
    def changeToSetting(self, value):
        self.manager.transition.direction = 'left'
        # modify the current screen to a different "name"
    	self.manager.current= 'settings'
    def quitApp(self, value):
        App.get_running_app().stop()
        

class MeetingroomScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout=GridLayout(cols=2)
        bmn = Button(text="Back to Main", on_press=self.changeToMain, halign = 'left',font_size = 30)
        self.layout.add_widget(bmn)
        bcls = Button(text="Classrooms", on_press=self.changeToClass, halign = 'left',font_size = 30)
        self.layout.add_widget(bcls)
        blib = Button(text="Library", on_press=self.changeToLibrary, halign = 'left',font_size = 30)
        self.layout.add_widget(blib)
        btn = Button(text="Quit", on_press=self.quitApp, halign = 'left',font_size = 30)
        self.layout.add_widget(btn)
        self.add_widget(self.layout)

        
    def changeToMain(self, value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
    	self.manager.current= 'main'
    def changeToClass(self, value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
    	self.manager.current= 'classrooms'
    def changeToLibrary(self, value):
        self.manager.transition.direction = 'down'
        # modify the current screen to a different "name"
    	self.manager.current= 'library'
    def quitApp(self, value):
        App.get_running_app().stop()
        
    
class LibraryScreen(Screen):
    def __init__(self, **kwargs): 
        Screen.__init__(self, **kwargs)
        self.layout=GridLayout(cols=2)
        bmn = Button(text="Back to Main", on_press=self.changeToMain, halign = 'left',font_size = 30)
        self.layout.add_widget(bmn)
        bcls = Button(text="Classrooms", on_press=self.changeToClass, halign = 'left',font_size = 30)
        self.layout.add_widget(bcls)
        blib = Button(text="Meeting Rooms", on_press=self.changeToMeeting, halign = 'left',font_size = 30)
        self.layout.add_widget(blib)
        btn = Button(text="Quit", on_press=self.quitApp, halign = 'left',font_size = 30)
        self.layout.add_widget(btn)
        self.add_widget(self.layout)

        
    def changeToMain(self, value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
    	self.manager.current= 'main'
    def changeToClass(self, value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
    	self.manager.current= 'classrooms'
    def changeToMeeting(self, value):
        self.manager.transition.direction = 'down'
        # modify the current screen to a different "name"
    	self.manager.current= 'meetingrooms'
    def quitApp(self, value):
        App.get_running_app().stop()


class BookingApp(App):
	def build(self):
            sm=ScreenManager()
            ms=MainScreen(name='main')
            clr=ClassroomScreen(name='classrooms')
            mtr=MeetingroomScreen(name='meetingrooms')
            lib=LibraryScreen(name='library')
            Clock.schedule_interval(clr.refresh, 10)
                        
            sm.add_widget(ms)
            sm.add_widget(clr)
            sm.add_widget(mtr)
            sm.add_widget(lib)
            sm.current='main'
            return sm


if __name__=='__main__':
	BookingApp().run()
