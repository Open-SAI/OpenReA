#*-* coding:utf-8 *-*
#qpy:kivy
import kivy
from jnius import autoclass
import time
from plyer.platforms.android import activity
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.widget import Widget

#class TextoHablado(App):
class TextoHablado(Widget):
    def build(self, Mensaje):
        self.mensaje_Recibido = str(Mensaje)
        self.Mi_Widget= Widget()
        self.local =autoclass('java.util.Locale')
        actividadPython = autoclass('org.renpy.android.PythonActivity')
        self.texto_hablado = autoclass('android.speech.tts.TextToSpeech')
        self.tts = self.texto_hablado(actividadPython.mActivity,None)
        for i in range (1,2,1):
            self.tts.setLanguage(self.local.ROOT)
            time.sleep(0.4)
            try:        
                self.tts.speak(self.mensaje_Recibido, self.texto_hablado.QUEUE_ADD,None)
                print "se encontro pero no funciona"
                if True:
                    time.sleep(0.4)
                    print "Si fuciono"
                while not True:
                    self.tts.speak(self.mensaje_Recibido, self.texto_hablado.QUEUE_ADD,None)
                    print "se encontro pero no funciona"
                    if True:
                        time.sleep(0.4)
                        print "Si fuciono"
                     
            except:
                print "no se encontro local"
                pass
        return self.Mi_Widget
        
#if __name__=='__main__':
 #   TextoHablado().run()

