#*-*coding:utf-8*-*
#qpy:kivy
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label 
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.camera import Camera

class ScreenLogin(RelativeLayout):
#class ScreenLogin(App):
    def build(self):
        self.opc = False
        self.opc1 = False
        self.cont1 = 0

        
        self.rl = RelativeLayout()
        self.lb  = Label(font_size="20 sp",pos_hint={'center_x': .5, 'center_y': .1} , markup=True)

#============================================================================
#esta parte es para agregar  la camaraen el layout
#============================================================================
#____________________________________________________________________________        
        cam =Camera(resolution=(640, 480), size_hint_x=1.2, size_hint_y=1, pos_hint={'center_x': .5, 'center_y': .5})
        self.rl.add_widget(cam)
#=============================================================================


#============================================================================
#esta parte es para agregar una imagen en el layout
#============================================================================
#____________________________________________________________________________        
#        self.img = Image()
#        self.img.source = "Imagenes/Screen1.png"
#        self.img.pos=(0,0)
#        self.rl.add_widget(self.img)
#____________________________________________________________________________
#=============================================================================
        
        self.rl.add_widget(self.lb)
        self.Procesos_Bluetooth()
        self.mensaje1 = "[color=ff3333] Coloque su llave en el lector."
        self.blueRequest = "Nada"
        Clock.schedule_interval(self.Cont1, 0.8) 
        Clock.schedule_interval(self.IDENTIFICADOR_P, 0.3)
        return self.rl


    # FUNCIÓN TIPO RELOJ PARA COLOCAR Y QUITAR LOS AVISOS
    def Cont1(self, dt):
        print self.cont1
        Mensaje = "a \r\n"
        try:
            ArduinoB.Escribir(Mensaje)
        except:
            pass
        
        try:            
            self.blueRequest =  ArduinoB.LeerCADENA() # LECTURA DEL BLUETOOTH ALMACENDA EN UNA VARIABLE            
        except:
            self.blueRequest = " 123142 "
            pass
        if ((self.blueRequest== "Nada")or(len(self.blueRequest)<5)):

            if (self.cont1 <= 2):
                print "Llamando el aviso"
                self.AvisON()
                self.cont1 = self.cont1 + 1
                
            if ((self.cont1 > 2)or(self.cont1 == 4)):
                print "Quitando el aviso"
                self.AvisOFF()
                self.cont1 = self.cont1 + 1
            
            if (self.cont1 > 4):
                self.cont1 = 0
                self.opc = False
                self.opc1 = False

                
        if ((len(self.blueRequest) != 0) and (self.blueRequest!= "Nada")):
            print "===========> la longitud de la puta variable es: " + str(len(self.blueRequest))
            print "NUID encontrada, Deteneiendo el hilo"
            Clock.unschedule(self.Cont1)
            print type(self.blueRequest)
            self.opc = False
            dataBlue = []
            dataBlue = self.blueRequest.split(" ")
            print dataBlue[0]
            print len(dataBlue)
            mensaje = ""
            for i in range (1, len(dataBlue), 1):
                mensaje = mensaje + str(dataBlue[i])
            print mensaje                
            self.mensaje1 = " [color=ff3333] NUID: " + str(mensaje)
            self.AvisON()
            self.blueRequest = str(mensaje)
            self.bufferLectura()

    # DEFINO UN BUFFER PARA LA LECTURA DEL BLUETOOTH
    def bufferLectura(self):
        lectura_del_Bluetooth = str(self.blueRequest)
        return lectura_del_Bluetooth

    # FUNCIÓN PARA ENCENDER LA LECTURA DE LA TARJETA NUEVAMENTE
    def ReiniciarLectura(self):
        self.blueRequest = "Nada"
        self.mensaje1 = "[color=ff3333] Coloque su llave en el lector."
        try:
            Clock.unschedule(self.Cont1)
        except:
            pass
        try:
            Clock.schedule_interval(self.Cont1, 0.8)
        except:
            pass


            
    #PONER EL AVISO
    def AvisON(self):
        if (self.opc == False):
            self.lb.text = str(self.mensaje1)
            self.opc = True

        if (self.opc == True):
            pass


    # QUITAR EL AVISO
    def AvisOFF(self):
        if (self.opc1 == False):
            self.lb.text = " "
            self.opc1 = True

        if (self.opc1 == True):
            pass


    #IDENTIFICADOR DE PROCESOS DEL BLUETOOTH
    def Procesos_Bluetooth(self):
        try:
            from Ardutooth import ArduinoBluetooth 
            global ArduinoB
            ArduinoB = ArduinoBluetooth()
            Mensaje = "Procesos Bluetooth Activados "
            print Mensaje 
            self.EncenderBluetooth()
        except:
            Mensaje = "Fallo al activar los procesos Arduino"
            print Mensaje
        pass
        
    #FUNCIÓN PARA ENCENDER EL BLUETOOTH     
    def EncenderBluetooth(self, *args):
        print "Llamado a prender"
        Dispo1 = "HC-05" #MODULO BLUETOOTH
        Dispo2 = "HC-06" #MODULO BLUETOOTH
        try:
            ArduinoB.obtenerCorrienteEnchufe(Dispo1)
            Mensaje = "Dispositivo conectado"
            print Mensaje
        except:
            Mensaje = "Dispositivo HC-05 NO ENCONTRADO PROBANDO EL HC-06 "
            print Mensaje
            #            ArduinoB.obtenerCorrienteEnchufe(Dispo1)
            #            pass
            try:
                
                ArduinoB.obtenerCorrienteEnchufe(Dispo2)
                Mensaje = "Dispositivo conectado"
                print Mensaje
            except:
                Mensaje = "Dispositivo HC-06 NO ENCONTRADO PASANDO A MODO AUTONOMO "
                print Mensaje
                #           ArduinoB.obtenerCorrienteEnchufe("HC-06")
                pass



    def ApagarBluetooth(self):
        try:
            ArduinoB.Cerrar()
        except:
            print "No se pudo cerrar el bluetooth."
        try:
            ArduinoB.__del__()
        except:
            pass

            
    #DECIDE CUANDO DEJAR O QUITAR LOS PROCESOS DEL SCREEN
    def IDENTIFICADOR_P(self, dt):
        #ABRO UN ARCHIVO Y LO ALMACENO EN UNA VARIABLE
        var = open("Datos/SCREEN.text", "r")
        self.lec = var.readline()
        print self.lec
        var.close()
        

        #PERMITE QUE EL SCREEN PERMANEZCA VIVO
        if self.lec == "True\n":
            print "Lectura verdadera desde El escreen de verificacion de llaves"
            pass

        if(self.lec == "False\n"):
            print "Lectura Falsa"
            try:
                self.blueRequest = "Nada"
                self.bufferLectura()
            except:
                pass
            try:                
                #QUITO EL HILO QUE DECIDE CUANDO DEJAR O QUITAR LOS PROCESOS DEL SCREEN
                Clock.unschedule(self.IDENTIFICADOR_P)
            except:
                pass
            try:
                #QUITO EL HILO DE LA FUNCIÓN TIPO RELOJ PARA COLOCAR Y QUITAR LOS AVISOS
                Clock.unschedule(self.Cont1)
            except: 
                pass
       #     try:
        #        ArduinoB.__del__()
         #   except:
          #      pass
            


class ScreenLogin1(RelativeLayout):
    def build(self):
        return  ScreenLogin()


#if __name__ =="__main__":
 #   ScreenLogin().run()
