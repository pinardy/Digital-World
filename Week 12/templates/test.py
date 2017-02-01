from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SimpleRoot(BoxLayout):
    def on_our_btn_release(self, text_input):
        text = Label(text="Hello, {}!".format(text_input))
        pop_up = Popup(title="Our Title!", content=text, size_hint=(.7, .7))
        pop_up.open()

class SimpleApp(App):
    def build(self):
        return SimpleRoot()

if __name__ == "__main__":
    SimpleApp().run()