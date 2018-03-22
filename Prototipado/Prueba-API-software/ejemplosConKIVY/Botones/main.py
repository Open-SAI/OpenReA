#*-*coding:utf-8*-*
import kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.app import App

class Botones(App):
    def build(self):
        global wdg
        global lbl
        global btn
        wdg = Widget()
        lbl = Label()
        btn = Button()
        btn.text= "llamado"
        btn.pos = (100,100)
        wdg.add_widget(lbl)
        wdg.add_widget(btn)
        btn.bind(on_press=self.ac_btn)
        return wdg

    def ac_btn(self, *args):
        lbl.text= "Me llamo el botón"
        lbl.pos = (200, 200)
        wdg.remove_widget(btn)


if __name__ == "__main__":
    Botones().run()
