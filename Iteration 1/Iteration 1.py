from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget 

class MyScreen(Widget):
    def screen(self):
        self.screen(text = 'screen')
    pass

class SayHello(App):

    def calc(self):
        print('calc')
     
    def build(self):
        self.window = GridLayout() # Adds widgets to Window 
        self.window.cols = 1

        # image widget
        self.window.add_widget(Image(source = 'testimage3.jpg'))

        # Label widget 
        self.greeting = Label(text = "enter your name")
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(multiline = False)
        self.window.add_widget(self.user)
    
        # button widget 
        self.button = Button(text = "greet")
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        #self.window.add_widget(MyScreen)
        return self.window
   
    def callback(self, event):

        self.greeting.text = "Hi " + self.user.text + "!"
        self.button.text = 'changed'
        print(self.user.text)
        name = self.user.text

if __name__ == "__main__":
    SayHello().run()
