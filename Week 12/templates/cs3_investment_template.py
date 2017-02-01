from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 


class Investment(App):

	def build(self):
		layout= GridLayout(cols=2)

		layout.add_widget(Label(text="Investment Amount", halign='left'))
		self.investAmt = TextInput(text='0.0')
		layout.add_widget(self.investAmt)

		layout.add_widget(Label(text="Years", halign='left'))
		self.yrs = TextInput(text='0.0')
		layout.add_widget(self.yrs)

		layout.add_widget(Label(text="Annual interest rate", halign='left'))
		self.annualIR = TextInput(text='0.0')
		layout.add_widget(self.annualIR)

		layout.add_widget(Label(text="Future Value", halign='left'))
		self.lblFutureVal = Label(text="0.0", halign='left')
		layout.add_widget(self.lblFutureVal)

		btn = Button(text="Calculate", on_press=self.calculate)
		layout.add_widget(btn)
		return layout # root widget

	def calculate(self, instance): # callback function
		invAmt = float(self.investAmt.text) # .text to access the text
		years = float(self.yrs.text) # REMEMBER THE .text !!!
		mthIntRate = (float(self.annualIR.text)/12)/100 # PUT THE .text, and divide by 100
		futureVal = invAmt*((1+mthIntRate)**(years*12))
		self.lblFutureVal.text= "%.2f"%futureVal


Investment().run() # obj instantiation