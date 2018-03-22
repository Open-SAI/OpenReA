#*-*coding:utf-8*-*
#qpy:kivy
import kivy
from kivy.uix.widget import Widget
from kivy.utils import platform
import os

if platform == 'linux':
    from gtts import gTTS
    tts = gTTS(text='Hola soy texto hablado', lang='es-es')
    tts.save("good.mp3")
    os.system("vlc good.mp3")
    print "yes"

if platform == 'android':
    from TextoHablado import *
    try: 
        TTs = TextoHablado().build("Hola soy texto hablado")
        print "Se encontro TTs"
    except: 
        print "Problemas con el textToSpeach"



