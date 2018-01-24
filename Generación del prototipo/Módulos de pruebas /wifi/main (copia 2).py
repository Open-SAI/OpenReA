#*-*coding:utf-8 *-*
#qpy:kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
from WifiOpensai import *        

class Principal(App):
    
    def build(self):        
        wg = Widget()
        lbl = Label()
        wg.add_widget(lbl)
        lbl.text =  "Iniciando Wifi"
        wifi  = WifiOpensai()

        ssid = wifi.ScanRedes()
        lbl.text = ssid
        return wg

if __name__ == "__main__":
    Principal().run()
