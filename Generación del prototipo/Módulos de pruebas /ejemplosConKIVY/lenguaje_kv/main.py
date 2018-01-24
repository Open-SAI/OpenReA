#*-* coding:utf-8*-*
from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.widget import Widget
from kivy.uix.label  import Label


Builder.load_string('''
BoxLayout:
    Label:
        text:"Hola mundo"
''')

class LabelOpen(Label):
    pass 

class LabelApp(App):
    def build(self):
       LabelOpen)

        return LabelOpen()

if __name__ == '__main__':
    LabelApp().run()
