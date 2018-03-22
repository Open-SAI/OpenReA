#*-*coding:utf-8*-*
import kivy
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.app import App
class Capas(App):
    def build(self):
        wdg = Widget()
        img = Image()
        img1 = Image()
        img2 = Image()
        wdg.add_widget(img)
        wdg.add_widget(img1)
        wdg.add_widget(img2)
        img.source = "img/kivy.jpeg"
        img.size = (600, 400)
        img.pos = (100, 50)
       
        img1.source = "img/linux.jpeg"
        img1.size = (100, 100)
        img1.pos = (140, 80)

        img2.source = "img/python.png"
        img2.size = (100, 100)
        img2.pos = (540, 80)

        wdg.remove_widget(img2)
        return wdg

if __name__ == "__main__":
    Capas().run()
