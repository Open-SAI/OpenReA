# *-*coding:utf-8 *-*
#qpy:kivy
#import sys
#sys.path.append('Datos')
#Módulo agregar usuario
#Desarrollado por Diego Alberto Parra Garzón
#Bogotá D.C., Colombia
# Esto es software libre licencia GPL3
# ________________________________________________________________________
# Para revisar si pudo agregar o no el usuario llame a la función
#                Como_va_la_cosa()
# La cuál devuelve ["nada", "nada"] Si no se han llenado los text input
# y si los text input ya se llenaron devuelve ["valor1", "valor2"]
#____________________________________________________________________

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class ScreenAgregarUser(App):
#class ScreenAgregarUser(RelativeLayout):
    
    def build(self):
        global rl1 #Layout principal del Screen 
        global rl2  #Layout para la interaccion con el usuario
        global txtIn1 #Text input user name
        global txtIn2 #text input identificacion user
        global btn # Boton para agregar los usuarios
        global lbl1 #Texto "Ingrese usuario"
        global lbl2 #texto "Ingrese Cédula "
        global lbl3 #texto "Advertensias que da la app "
        
        self.comoVa = ["nada", "nada"]
        self.Como_va_la_cosa()

            
        rl1 = RelativeLayout()
        rl2 = RelativeLayout()
       
        #Inicializo los wadgets que necesita la app
        #Inicializo los text input
        txtIn1 = TextInput(size_hint=(0.36, 0.2), pos=(500,300), text="", font_size="20dp", multiline=False)
        txtIn2 = TextInput(size_hint=(0.36, 0.2), pos=(500,170), text="", font_size="20dp", multiline=False, input_type="number")

        # Agrego los label de los text input
        lbl1 = Label(font_size="21", pos=(230, 130), text="Nombre completo usuario:")
        lbl2 = Label(font_size="21", pos=(230, 0), text="Clave dada por la empresa:")
        lbl3 = Label(font_size="24", pos=(-100, -150), text="")
        # Inicializo el boton
        btn = Button(size_hint=(0.36, 0.2), pos=(500, 30), text="Agregar usuario", font_size="24dp")


        #agrego el wadget de interfaz de usuario al widget principal
        rl1.add_widget(rl2)

        #agrego el wadget de interfaz autonoma al widget principal
                       

        #LLamo a la función interaccionAUTONOMA() para agregar los wadget autonomos al widget principal


        rl2.add_widget(lbl3)
        self.interaccionUSER()
        return rl1

    def interaccionUSER(self):
        rl2.add_widget(txtIn1)
        rl2.add_widget(txtIn2)
        rl2.add_widget(lbl1)
        rl2.add_widget(lbl2)
        rl2.add_widget(btn)
        btn.bind(on_press=self.AgregarUsuario)

    
    def AgregarUsuario(self, *args):
        print "Me llamo"
        valor1 = txtIn1.text
        valor2 = txtIn2.text
        if (valor1 == "")or(valor2== ""):
            mensaje= "Las casillas no puede estar vacias."
            print mensaje
            lbl3.text= mensaje
        if (valor1 != "")and(valor2 != ""):
            btn.unbind(on_press=self.AgregarUsuario)
            print "Listo el nombre  "
            self.comoVa= [str(valor1), str(valor2)]
            self.Como_va_la_cosa()

            rl1.clear_widgets()
            

    def Como_va_la_cosa(self):
        comoVa1 = self.comoVa[0]
        comoVa2 = self.comoVa[1]
        print self.comoVa
        return self.comoVa
        
            
if __name__ =="__main__":
    ScreenAgregarUser().run()
