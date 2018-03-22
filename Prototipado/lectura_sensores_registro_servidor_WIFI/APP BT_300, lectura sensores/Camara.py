#*-*coding:utf-8*-*
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.lang import Builder


CamaraVideo ='''
<emCamara>:
    Camera:
        index: 0
        resolution: 680, 480
        size: 1000, 600
        pos: -100, 0
        play: True

'''


Builder.load_string(CamaraVideo)

class emCamara(Widget):
    pass

#class MiCamara(App):
class MiCamara(Widget):
    def build(self):
        return emCamara()

if __name__ == '__main__':
    MiCamara().build()
