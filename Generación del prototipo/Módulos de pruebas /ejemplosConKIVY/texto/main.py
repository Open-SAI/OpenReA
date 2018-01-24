#*-*coding:utf-8*-*
import kivy
from kivy.uix.label import Label
from kivy.uix.widget import  Widget
from kivy.app import App

class Texto(App):
    def build(self):
        wdg = Widget()
        lbl = Label()
        lbl.markup = True
        lbl.pos = (100,100)
        lbl.text = "Hola soy un Label"
        lbl.color = (1, 0.5,0.5 ,1)
        lbl.font_size= "22sp"
        wdg.add_widget(lbl)
        return wdg

if __name__ == "__main__":
    Texto().run()
