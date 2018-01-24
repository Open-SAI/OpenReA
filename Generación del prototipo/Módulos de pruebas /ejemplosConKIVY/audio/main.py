#*-*coding:utf-8*-*
#qpy:kivy
import kivy
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.app import App

class Reproductor(App):
    def build(self):
        wg = Widget()
        sound = SoundLoader().load("playlist/VivaldiSummer-JohnHarrisonviolin.mp3")
        sound.volume = 3
        sound.play()
        return wg

if __name__ == "__main__":
    Reproductor().run()
        
