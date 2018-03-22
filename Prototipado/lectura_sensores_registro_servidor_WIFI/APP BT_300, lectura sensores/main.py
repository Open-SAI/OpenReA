#*-*coding:utf-8 *-*
#qpy:kivy
#kivy.require('1.9.1')

from Acelerometro import * 
from Camara import *
import kivy 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config 
from kivy.uix.camera import Camera
from kivy.uix.relativelayout import RelativeLayout
import random
from kivy.clock import Clock, mainthread
from kivy.uix.image import Image
from plyer import compass
import math

from jnius import autoclass

class OpReA(App):
    def build(self):
        self.acx = 0
        self.acy = 0
        self.acz = 0
        self.lbl1 = Label()
        self.lbl2 = Label()
        self.lbl1.pos = (-100, 100)
        self.lbl2.pos = (-100, 0)
        self.wd1 = RelativeLayout()
        self.Camara()
        self.LogoSena()
        self.wd1.add_widget(self.lbl1)
        self.SensorCM()
        self.wd1.add_widget(self.lbl2)
        self.AceleroMetro()


        return self.wd1


    def Camara(self):   # Función que carga la ímagen de la cámara 
        wige = Widget()
        Scat1 = Scatter(scale=3.5, do_rotation=False, do_scale=False, do_translation_y=False,  do_translation_x=False, size=(1000,600))        
        camw = Widget()  #Create a camera Widget
        cam = Camera(resolution=(320, 240),size=(1000,600), pos=(-250,-140), play=True)
        camw.add_widget(cam)
        Scat1.add_widget(camw)
        wige.add_widget(Scat1)        
        self.wd1.add_widget(wige)

    def LogoSena(self):
        wige1 = Widget()
        Scat1 = Scatter(do_rotation=False, do_scale=False, do_translation_y=False,  do_translation_x=False, size=(100,60))        
        Anim1 = Image()
        Anim1.pos= (200, 550)
        Anim1.source = "Img/logosena2.png"
        Scat1.add_widget(Anim1)
        wige1.add_widget(Scat1)     
        self.wd1.add_widget(wige1)
        
    def AceleroMetro(self):
        global maquina
        global acx, acy, acz

        try:
            maquina = Acelerometro()
            if (maquina.Hardware() == True):
                print "Hardware compatible con acelerometro"
                Clock.schedule_interval(self.disparo2, 0.4)

                

            else:
                print "No es COMPATIBLE"
        except:
            pass

    def SensorCM(self):
        try: 
            compass.enable()
            if True:
                print "es cierto"
                self.tetha=0
                Clock.schedule_interval(self.disparo1, 0.4)

        except NotImplementedError:
            import traceback
            traceback.print_exc()
            status = "No reconoce el sensor magnetico en su dispositivo"
            print "No reconoce el compas"
            pass

    def disparo1(self, dt): 
        self.LecturaCM()

    def disparo2(self, dt):
        self.LecturaAcelerometro()

    def LecturaAcelerometro(self):
        print "Acelerometro encontrado"
        print "Empezando la captura"
        acx, acy, acz = maquina.Disparador()
        print "aceleracion en x", acx
        print "aceleracion en y", acy
        print "aceleracion en z", acz
        self.acx = acx
        self.acy = acy
        self.acz = acz
        Vector_aceleracion = "Aceleracion en x: " + str(acx) + "\nAceleracion en y: " + str(acy) + "\nAceleracion en z: " + str(acz) 
        self.lbl2.text = "soy texto 2"
        self.lbl2.text = Vector_aceleracion

    def LecturaCM(self):
        x,y,z = compass.orientation
        try:
            xf = round(x,  3)
            yf = round(y,  3)
            zf = round(z,  3)
            self.Bx = xf
            self.By = yf
            self.Bz = zf
            self.lbl1.text = "Campo Magnético \n\n       Bx = "+str(xf)+"\n"+"       By = "+str(yf)+"\n"+"       Bz = "+str(zf)#+"\n"+"       tetha=  "+ str(self.tetha)
        except: 
            print "No hay ningun dato todavia espere"


        try:
            self.wd1.remove_widget(lol)

        except:
            pass

      





if __name__ == '__main__':
    OpReA().run()
