#*-*coding:utf-8*-*
import kivy
from kivy.uix.camera import Camera
from kivy.uix.widget import Widget
from kivy.app import App

class Camara(App):
    def build(self):
        wdg = Widget()
        '''
        cam = Camera()
        cam.pos = (50,100)
        cam.resolution = (680, 480)
        cam.size = 700, 680
        cam.play = True
        '''
        cam = Camera(resolution=(320, 240),size=(1000,600), pos=(-350,-150), play=True)
        wdg.add_widget(cam)
        cam.size = (800, 600)
        return wdg

if __name__ == "__main__":
    Camara().run()
