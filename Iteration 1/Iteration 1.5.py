import kivy 
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

class Display(ScreenManager):

    mainname1 = ObjectProperty(None)
    mainname2 = ObjectProperty(None)

    def buttonclicked(self):
        print('First Name: ', self.mainname1.text, 'Last Name: ', self.mainname2.text)
        self.mainname1.text = ''
        self.mainname2.text = ''


class MyApp(App):

    def build(self):
        return Display()

  

if __name__ == "__main__":
    MyApp().run()
